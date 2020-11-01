from flask import jsonify
from app.api_v1 import bp
from .utils import get_supported_languages, get_supported_frameworks, get_supported_modules


@bp.route('/languages')
def supported_languages():
    return jsonify(get_supported_languages())


@bp.route('/languages/<language>')
def supported_frameworks(language):
    return jsonify(get_supported_frameworks(language))


@bp.route('/languages/<language>/<framework>')
def supported_modules(language, framework):
    return jsonify(get_supported_modules(language, framework))
