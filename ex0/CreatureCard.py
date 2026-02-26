from typing import Dict, Any, Union
from .Card import Card, Rarity


class CreatureCard(Card):

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.__attack: Union[int, float] = 0
        self.__health: Union[int, float] = 0
        self.attack = attack
        self.health = health

    def __get_attack(self) -> Union[int, float]:
        return self.__attack

    def __set_attack(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Attack must be a positive integer")
        self.__attack = (
            float("inf") if self.rarity == Rarity.HAMID.value else value
        )

    def __get_health(self) -> Union[int, float]:
        return self.__health

    def __set_health(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Health must be a positive integer")
        self.__health = (
            float("inf") if self.rarity == Rarity.HAMID.value else value
        )

    attack = property(__get_attack, __set_attack)
    health = property(__get_health, __set_health)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        mana: int = int(game_state.get("mana", 0))
        if self.is_playable(mana):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": game_state.get("effect", "Creature summoned"),
                "remaining mana": mana - self.cost
            }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": None,
            "remaining mana": 0
        }

    def attack_target(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict[str, Union[str, int, float]]:
        info: Dict[str, Union[str, int, float]] = dict(super().get_card_info())
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
