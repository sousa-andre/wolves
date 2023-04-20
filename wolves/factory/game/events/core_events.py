from dataclasses import dataclass
from typing import Any, List

from wolves.factory.game.events import BaseEvent


@dataclass
class GameJoined(BaseEvent):
    id: str
    server_url: str
    player_count_for_language: int
    player_count_for_gamemode: int

    @staticmethod
    def from_json(data, _):
        return GameJoined(
            id=data['gameId'],
            server_url=data['serverUrl'],
            player_count_for_language=data['onlinePlayerCountForLanguage'],
            player_count_for_gamemode=data['onlinePlayerCountForGameMode']
        )


# LOBBY
@dataclass
class VotingStarted(BaseEvent):
    needed: int
    votes: Any

    @staticmethod
    def from_json(data, _):
        VotingStarted(needed=data['needed'], votes=data['votes'])


@dataclass
class GameSettingsChanged(BaseEvent):
    roles: List[str]