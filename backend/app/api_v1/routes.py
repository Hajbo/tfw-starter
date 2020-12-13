from flask import jsonify, request, send_file, make_response
from app.api_v1 import bp
from avatao_startr.main.assembler import Assembler
from avatao_startr.tfw.starter_kits.utils import (
    get_supported_language_names,
    get_framework_names_for_language,
    get_supported_modules,
)


@bp.route("/languages", methods=["GET"])
def supported_languages():
    return jsonify({"supported_languages": get_supported_language_names()})


@bp.route("/languages/<language>", methods=["GET"])
def supported_frameworks(language):
    return jsonify(
        {
            "language": language,
            "supported_frameworks": get_framework_names_for_language(language),
        }
    )


@bp.route("/languages/<language>/frameworks/<framework>", methods=["GET"])
def supported_modules(language, framework):
    return jsonify(get_supported_modules(language, framework))


@bp.route("/assemble", methods=["POST"])
def assemble_starter():
    language = request.json.get("language")
    framework = request.json.get("framework")
    dependency_list = request.json.get("modules")
    with Assembler() as assembler:
        response = make_response(
            send_file(
                assembler.assemble_and_zip_starter(
                    language, framework, dependency_list
                ),
                as_attachment=True,
            )
        )
    response.headers[
        "Access-Control-Expose-Headers"
    ] = "content-type, content-disposition"
    return response
