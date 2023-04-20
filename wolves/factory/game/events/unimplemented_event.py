from dataclasses import dataclass
from typing import Any

from wolves.factory.game.events.base_event import BaseEvent


@dataclass
class UnimplementedEvent(BaseEvent):
    event: str
    data: Any

    @staticmethod
    def from_json(data, event_type):
        return UnimplementedEvent(data=data, event=event_type)
