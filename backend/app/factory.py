from flask import Flask

from app.config import AppConfig


def create_app(config_class=AppConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.test import bp as test_bp
    app.register_blueprint(test_bp, url_prefix='/')
    
    return app

