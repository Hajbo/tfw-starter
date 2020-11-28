from avatao_startr.main.framework_config_base import FrameworkConfigBase

class FrameworkConfig(FrameworkConfigBase):
    @property
    def supervisor_command(self):
        return "node app.js"
