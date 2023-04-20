from wolves.factory.game.events.chat_events import PublicChatMessage
from wolves.factory.game.events.ungrouped_events import UserBanned, GamePlayersKilled
from wolves.factory.game.events.unimplemented_event import UnimplementedEvent


class EventFactory:
    MAPPINGS = {
        'game:chat-public:msg': PublicChatMessage,
        'game-players-killed': GamePlayersKilled,
        'error-user-banned': UserBanned,
    }

    @classmethod
    def create(cls, event_string):
        return cls.MAPPINGS.get(event_string, UnimplementedEvent)
