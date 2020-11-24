import secrets


class AppConfig:
    SECRET_KEY = secrets.token_hex(64)
