from ex0 import Card
from typing import Dict, Union


class ArtifactCard(Card):
    """Concrete implementation of an artifact card."""

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        self.__durability: int = 0
        self.__effect: str = "None"
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    @property
    def durability(self) -> int:
        return self.__durability

    @durability.setter
    def durability(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Durability must be a positive integer")
        self.__durability = value

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Effect must be a non-empty string")
        self.__effect = value

    def play(
        self, game_state: Dict[str, Union[str, int]]
    ) -> Dict[str, Union[str, int]]:
        slots: int = game_state.get("artifact_slots", 0)
        mana: int = game_state.get("mana", 0)
        effect: int = game_state.get("effect", "None")
        can_play: bool = (self.is_playable(mana) and slots > 0)

        return {
            "card_played": self.name,
            "mana_used": self.cost if can_play else 0,
            "effect": effect
        }

    def activate_ability(self) -> Dict[str, Union[str, int]]:
        if self.__durability <= 0:
            return {"status": "broken"}
        self.__durability -= 1
        return {
            "ability": self.__effect,
            "remaining_durability": self.__durability
        }
