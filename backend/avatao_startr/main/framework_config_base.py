from abc import ABC, abstractmethod


class FrameworkConfigBase(ABC):
    @property
    def docker_commands(self):
        return []

    @property
    @abstractmethod
    def supervisor_command(self):
        return ""
