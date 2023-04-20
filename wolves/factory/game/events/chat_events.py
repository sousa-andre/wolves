from dataclasses import dataclass
from typing import Optional

from wolves.factory.game.events.base_event import BaseEvent


@dataclass
class PublicChatMessage(BaseEvent):
    id: str
    msg_key: Optional[str]
    msg: Optional[str]

    @staticmethod
    def from_json(data, _):
        return PublicChatMessage(id=data['id'], msg_key=data.get('msgKey'), msg=data.get('msg'))

