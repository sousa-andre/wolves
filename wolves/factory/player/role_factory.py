from wolves.factory.player.roles.base.unimplemented_role import UnImplementedRole
from wolves.factory.player.roles.village.medium import Medium
from wolves.factory.player.roles.village.others import Jailer, Vigilante, NightmareWolf, AuraSeer, AlphaWereWolf, \
    Detective


class RoleFactory:
    MAPPINGS = {
        'medium': Medium,
        'jailer': Jailer,
        'vigilante': Vigilante,
        'nightmare-werewolf': NightmareWolf,
        'aura-seer': AuraSeer,
        'alpha-werewolf': AlphaWereWolf,
        'detective': Detective,
    }

    @classmethod
    def create(cls, role_string):
        return cls.MAPPINGS.get(role_string, UnImplementedRole)
