from abc import ABC, abstractmethod
from importlib import import_module
from typing import List
from avatao_startr.main.framework_config_base import FrameworkConfigBase


class LanguageConfigBase(ABC):
    def __init__(self, language, framework, webservice_folder_path):
        self._language = language
        self._framework = framework
        self._webservice_folder_path = webservice_folder_path
        self._framework_config = self.__init_framework_config(language, framework)

    def __init_framework_config(
        self, language_folder, framework_folder
    ) -> FrameworkConfigBase:
        package = (
            "avatao_startr.tfw.starter_kits."
            f"{language_folder}.{framework_folder}.framework_config"
        )
        return import_module(package).FrameworkConfig()

    @classmethod
    def __run_script(self, script_name) -> None:
        import_module(f"avatao_startr.scripts.{script_name}").run()

    @property
    def docker_commands(self) -> List[str]:
        commands = []
        commands.extend(self._framework_config.docker_commands)
        commands.extend(self._docker_commands)
        return commands

    @property
    def supervisor_command(self) -> str:
        return self._framework_config.supervisor_command

    @property
    def _docker_commands(self) -> List[str]:
        return []

    @property
    def dockerfile_template_location(self) -> str:
        return None

    @abstractmethod
    def install_modules(self, module_list) -> None:
        pass
