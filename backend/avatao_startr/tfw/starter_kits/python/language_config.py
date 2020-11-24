import os
from avatao_startr.main.language_config_base import LanguageConfigBase


class LanguageConfig(LanguageConfigBase):
    def install_modules(self, module_list):
        self._module_installation_commands = [
            'RUN python3 -m pip install -r "${TFW_WEBSERVICE_DIR}/requirements.txt"'
        ]
        with open(
            os.path.join(self._webservice_folder_path, "requirements.txt"),
            "w+",
        ) as requirements:
            for module in module_list:
                requirements.write(f'{module.get("name")}=={module.get("version")}\n')
