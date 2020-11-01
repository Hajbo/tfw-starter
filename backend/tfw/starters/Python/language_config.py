import os
from main.starter_config.language_config_base import LanguageConfigBase


class LanguageConfig(LanguageConfigBase):

    def install_modules(self, module_list):
        self._module_installation_commands = [
            'RUN python3 -m pip install -r "${TFW_WEBSERVICE_DIR}/requirements.txt"'
        ]
        with open(os.path.join(os.environ.get('TFW_STARTER_WEBSERVICE_DESTINATION'), 'requirements.txt'), 'w+') as requirements:
            for module in module_list:
                requirements.write(f'{module.get("name")}=={module.get("version")}\n')
