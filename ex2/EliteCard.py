from ex0.Card import Card
from .Magical import Magical
from .Combatable import Combatable
from typing import Dict, List, Union


class EliteCard(Card, Combatable, Magical):
    """EliteCard with defense_power acting as a protection layer."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        attack_power: int, defense_power: int
    ) -> None:
        """Initializes EliteCard with combat and magic capabilities.

        Args:
            name: The name of the card.
            cost: The mana cost of the card.
            rarity: The rarity level of the card.
            attack_power: The physical damage strength.
            defense_power: The defensive capability of the card.
        """
        super().__init__(name, cost, rarity)
        self.__attack_power: int = 0
        self.__defense_power: int = 0

        self.attack_power = attack_power
        self.defense_power = defense_power

    @property
    def attack_power(self) -> int:
        """Gets the attack power."""
        return self.__attack_power

    @attack_power.setter
    def attack_power(self, value: int) -> None:
        """Sets the attack power."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Attack power must be a non-negative integer")
        self.__attack_power = value

    @property
    def defense_power(self) -> int:
        """Gets the defense power."""
        return self.__defense_power

    @defense_power.setter
    def defense_power(self, value: int) -> None:
        """Sets the defense power."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Defense power must be a non-negative integer")
        self.__defense_power = value

    def play(self, game_state: Dict[str, int]) -> Dict[str, Union[str, int]]:
        """Plays the card using game_state data.

        Args:
            game_state: Current state of the game.

        Returns:
            Dictionary with deployment results.
        """
        player_mana = int(game_state.get("mana", 0))
        is_allowed = self.is_playable(player_mana)

        return {
            "card": self.name,
            "status": "deployed" if is_allowed else "failed",
            "mana_cost": self.cost,
            "current_defense": self.__defense_power
        }

    def attack(self, target: str) -> Dict[str, Union[str, int]]:
        """Executes attack action.

        Args:
            target: The target of the attack.

        Returns:
            Dictionary with attack stats.
        """
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.__attack_power,
            "type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Union[str, int]]:
        """Uses defense_power to block incoming damage.

        Args:
            incoming_damage: Damage value to process.

        Returns:
            Dictionary showing damage absorbed by defense_power.
        """
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("Attack power must be a non-negative integer")

        blocked = min(self.__defense_power, incoming_damage)
        self.__defense_power -= blocked
        taken = incoming_damage - blocked

        return {
            "defender": self.name,
            "damage_blocked": blocked,
            "damage_taken": taken,
            "remaining_defense": self.__defense_power
        }

    def get_combat_stats(self) -> Dict[str, int]:
        """Returns combat related stats."""
        return {
            "attack": self.__attack_power,
            "defense": self.__defense_power
        }

    def cast_spell(
        self, spell_name: str, targets: List[str]
    ) -> Dict[str, str]:
        """Casts a spell from the card.

        Args:
            spell_name: Name of the spell.
            targets: List of targets.

        Returns:
            Dictionary with spell results.
        """
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "action": "magic_cast"
        }

    def channel_mana(self, amount: int) -> Dict[str, Union[str, int]]:
        """Increases defense_power (channeling).

        Args:
            amount: Amount to increase defense by.

        Returns:
            Dictionary with updated defense status.
        """
        self.__defense_power += amount
        return {
            "action": "channeling",
            "added_defense": amount,
            "total_defense": self.__defense_power
        }

    def get_magic_stats(self) -> Dict[str, int]:
        """Returns magic related stats."""
        return {"current_energy": self.__defense_power}
