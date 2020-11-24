import secrets


class AppConfig:
    SECRET_KEY = secrets.token_hex(64)
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True
