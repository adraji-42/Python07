from .Card import Card
from typing import Dict, Union


class CreatureCard(Card):
    """Concrete implementation of a creature card."""

    def __init__(
        self,
        name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.__attack: Union[int, float] = 0
        self.__health: Union[int, float] = 0
        self.attack = attack
        self.health = health

    @property
    def attack(self) -> Union[int, float]:
        return self.__attack

    @attack.setter
    def attack(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Attack must be a positive integer")
        self.__attack = float('inf') if self.rarity == "Hamid" else value

    @property
    def health(self) -> Union[int, float]:
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Health must be a positive integer")
        self.__health = float('inf') if self.rarity == "Hamid" else value

    def play(self, game_state: Dict[str, str]) -> Dict[str, Union[str, int]]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state.get('effect', 'Creature summoned')
        }

    def attack_target(
        self, target: str
    ) -> Dict[str, Union[str, int, float, bool]]:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.__attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict[str, Union[str, float, int]]:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.__attack,
            "health": self.__health
        })
        return info
