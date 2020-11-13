from main.starter_config import FrameworkConfigBase


class FrameworkConfig(FrameworkConfigBase):
    @property
    def supervisor_command(self):
        return "python3 app.py"
