import os
from abc import ABC, abstractmethod
from functools import cached_property
from importlib import import_module


class LanguageConfigBase(ABC):

    def __init__(self, language, framework):
        self._language = language
        self._framework = framework
        self._framework_config = self.__init_framework_config(language, framework)
    
    def __init_framework_config(self, language, framework):
        return import_module(f'tfw.starters.{language}.{framework}.framework_config').FrameworkConfig()

    @classmethod
    def __run_script(self, script_name):
        import_module(f'scripts.{script_name}').run()

    @property
    def docker_commands(self):
        commands = []
        commands.extend(self._framework_config.docker_commands)
        commands.extend(self._docker_commands)
        commands.extend(getattr(self, '_module_installation_commands', []))
        return commands

    @property
    def supervisor_command(self):
        return self._framework_config.supervisor_command

    @property
    def _docker_commands(self):
        return []
    
    @property
    def dockerfile_template_location(self):
        return os.environ.get('TFW_STARTER_DOCKERFILE_SOURCE')

    @abstractmethod
    def install_modules(self, module_list):
        """
            Do operations on files (e.g. edit package.js / requirements.txt)
                and if needed, set self._module_installation_commands to a 
                list of strings ['docker command 1', 'docker command 2']
        """
        pass
