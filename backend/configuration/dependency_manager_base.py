from abc import ABC, abstractmethod


class DependencyManagerBase(ABC):

    def __init__(self, framework):
        self._framework_config_handler = self.__load_config_handler(framework)
        self._extra_modules = None
    
    def __load_config_handler(self, framework):
        return 1

    @classmethod
    def __run_dependency_script(self, script_name):
        pass

    @abstractmethod
    def install_modules(self):
        """ Return a list of string (docker commands) for templating (e.g. Python pip install string)
            Return None if module installation doesn't need docker (e.g. nodejs package.json extension)
        """
        pass

    @classmethod
    @abstractmethod
    def load_supported_modules(self, framework):
        """ Language specific module loading from dependencies.json
            This is needed since the needed attributes are different (e.g. maven needs groupid besides name and version)
            Name and version are mandatory
        """
        pass