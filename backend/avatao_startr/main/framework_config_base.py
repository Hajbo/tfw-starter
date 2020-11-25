from abc import ABC, abstractmethod
from typing import List


class FrameworkConfigBase(ABC):
    @property
    def docker_commands(self) -> List[str]:
        return []

    @property
    @abstractmethod
    def supervisor_command(self) -> str:
        return ""
