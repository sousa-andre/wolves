from abc import abstractmethod, ABC
from typing import Any


class BaseEvent(ABC):
    @staticmethod
    @abstractmethod
    def from_json(data: Any, extra):
        pass
