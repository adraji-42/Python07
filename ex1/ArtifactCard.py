from ex0 import Card
from typing import Dict, Any


class ArtifactCard(Card):

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.__durability: int = 0
        self.__effect: str = "Unknow"
        self.durability = durability
        self.effect = effect

    def __get_durability(self) -> int:
        return self.__durability

    def __set_durability(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Durability must be a positive integer")
        self.__durability = value

    def __get_effect(self) -> str:
        return self.__effect

    def __set_effect(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Effect must be a non-empty string")
        self.__effect = value.strip()

    durability = property(__get_durability, __set_durability)
    effect = property(__get_effect, __set_effect)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        mana: int = int(game_state.get("mana", 0))
        if self.is_playable(mana) and self.durability > 0:
            self.durability -= 1
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect,
                "remaining_durability": self.durability,
                "remaining_mana": mana - self.cost
            }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": None,
            "remaining_durability": self.durability,
            "remaining_mana": mana
        }

    def activate_ability(self) -> Dict[str, Any]:
        if self.durability > 0:
            self.durability -= 1
            return {
                "ability_activated": self.effect,
                "remaining_durability": self.durability
            }
        return {
            "ability_activated": None,
            "remaining_durability": 0
        }

    def get_card_info(self) -> Dict[str, Any]:
        info: Dict[str, Any] = super().get_card_info()
        info.update({
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect
        })
        return info
