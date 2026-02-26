from ex0 import Card
from typing import Any, Dict, List


class SpellCard(Card):

    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.__effect_type: str = "Unknow"
        self.effect_type = effect_type

    def __get_effect_type(self) -> str:
        return self.__effect_type

    def __set_effect_type(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Effect type must be a non-empty string")
        self.__effect_type = value.strip()

    effect_type = property(__get_effect_type, __set_effect_type)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        mana: int = int(game_state.get("mana", 0))
        if self.is_playable(mana):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type,
                "remaining_mana": mana - self.cost
            }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": None,
            "remaining_mana": mana
        }

    def resolve_effect(self, targets: List[str]) -> Dict[str, Any]:
        return {
            "effect_type": self.effect_type,
            "targets": targets,
            "status": "resolved"
        }

    def get_card_info(self) -> Dict[str, Any]:
        info: Dict[str, Any] = super().get_card_info()
        info.update({
            "type": "Spell",
            "effect_type": self.effect_type
        })
        return info
