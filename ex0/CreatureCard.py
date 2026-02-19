from typing import Any, Dict, Union
from .Card import Card


class CreatureCard(Card):
    """Concrete implementation of a creature card.

    Attributes:
        attack: The damage the creature deals.
        health: The life points of the creature.
    """

    def __init__(
        self,
        name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        assert isinstance(attack, int), "Attack must be an integer"
        assert attack >= 0, "Attack must be positive"
        self.__attack: Union[int, float] = (
            attack if self.rarity != "Hamid" else float('inf')
        )

        assert isinstance(health, int), "Health must be an integer"
        assert health >= 0, "Health must be positive"
        self.__health: Union[int, float] = (
            health if self.rarity != "Hamid" else float('inf')
        )

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, attack) -> int:

        assert isinstance(attack, int), "Attack must be an integer"
        assert attack >= 0, "Attack must be positive"
        self.__attack: Union[int, float] = (
            attack if self.rarity != "Hamid" else float('inf')
        )

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health) -> int:
        assert isinstance(health, int), "Health must be an integer"
        assert health >= 0, "Health must be positive"
        self.__health: Union[int, float] = (
            health if self.rarity != "Hamid" else float('inf')
        )

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        if 'effect' not in game_state:
            raise KeyError(
                "The Creature Card object for the game state "
                "does not contain an 'Effect' key in the game interface."
            )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state['effect']
        }

    def attack_target(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.__attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.__attack,
            "health": self.__health
        })
        return info
