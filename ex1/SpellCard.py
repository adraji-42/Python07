from ex0 import Card
from typing import Any, Dict, List


class SpellCard(Card):
    """Concrete implementation of a spell card."""

    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        self.__effect_type: str = "None"
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    @property
    def effect_type(self) -> str:
        return self.__effect_type

    @effect_type.setter
    def effect_type(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Effect type must be a non-empty string")
        self.__effect_type = value.strip().capitalize()

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        available_mana = game_state.get("mana", 0)
        if not self.is_playable(available_mana):
            raise ValueError(f"Not enough mana to cast {self.name}")

        targets = game_state.get("targets", [])
        return {
            "card_played": self.name,
            "type": "Spell",
            "effect_type": self.__effect_type,
            "mana_remaining": available_mana - self.cost,
            "targets_hit": len(targets) if isinstance(targets, list) else 0
        }

    def resolve_effect(self, targets: List[str]) -> Dict[str, Any]:
        return {
            "effect": self.__effect_type,
            "targets_affected": targets,
            "resolved": True
        }
