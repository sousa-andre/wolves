from dataclasses import dataclass
from typing import List

from wolves.factory.game.events.base_event import BaseEvent


@dataclass
class GamePlayersKilledVictim(BaseEvent):
    target_player_id: str
    cause: str

    @staticmethod
    def from_json(data, _):
        return GamePlayersKilledVictim(target_player_id=data['targetPlayerId'], cause=data['cause'])


@dataclass
class GamePlayersKilled(BaseEvent):
    victims: List[GamePlayersKilledVictim]

    @staticmethod
    def from_json(data, _):
        return GamePlayersKilled(victims=[GamePlayersKilledVictim.from_json(victim, _) for victim in data['victims']])


@dataclass
class UserBanned(BaseEvent):
    until_time: str
    reason: str
    reason_message: str

    @staticmethod
    def from_json(data, _):
        return UserBanned(until_time=data['bannedUntilTime'], reason=data['banReason'], reason_message=data['banReasonMsg'])



