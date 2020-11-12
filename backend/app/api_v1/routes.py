from flask import jsonify, request, current_app, send_file
from app.api_v1 import bp
from .utils import get_supported_languages, get_supported_frameworks, get_supported_modules


@bp.route('/languages', methods=['GET'])
def supported_languages():
    return jsonify(get_supported_languages())


@bp.route('/languages/<language>', methods=['GET'])
def supported_frameworks(language):
    return jsonify(get_supported_frameworks(language))


@bp.route('/languages/<language>/<framework>', methods=['GET'])
def supported_modules(language, framework):
    return jsonify(get_supported_modules(language, framework))


@bp.route('/assemble', methods=['POST'])
def assemble_starter():
    language = request.json.get('language')
    framework = request.json.get('framework')
    modules = request.json.get('modules')
    return send_file(current_app.assembler.assemble_and_zip_starter(language, framework, modules), as_attachment=True)


@bp.route('/test')
def test_assemble():
    language = 'python'
    framework = 'flask'
    modules = [
        {'name': 'Flask', 'version': '1.1.2'},
        {'name': 'requests', 'version': '2.24.0'}
    ]
    return send_file(current_app.assembler.assemble_and_zip_starter(language, framework, modules), as_attachment=True)
