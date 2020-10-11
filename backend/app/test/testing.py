from flask import jsonify, send_file

from app.test import bp

@bp.route('/test')
def test():
    from tfw_assembler import Assembler
    a = Assembler('Python', 'Flask')
    return send_file(a.generate_zip())
