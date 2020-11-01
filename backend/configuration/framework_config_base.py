from abc import ABC, abstractmethod


class FrameworkConfigBase(ABC):
    
    @property
    @abstractmethod
    def docker_commands(self):
        pass

    @property
    @abstractmethod
    def supervisord_run_command(self):
        pass
