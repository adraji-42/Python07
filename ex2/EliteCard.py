from ex0 import Card, Rarity
from .Magical import Magical
from .Combatable import Combatable
from typing import Dict, Any, List


class EliteCard(Card, Combatable, Magical):

    def __init__(
        self, name: str, cost: int, rarity: str,
        attack_power: int, health: int, wopen
    ) -> None:
        super().__init__(name, cost, rarity)
        self.__wopen = wopen
        self.__health: int = 10
        self.__attack_power: int = 0
        self.health = health
        self.attack_power = attack_power

    def __get_wopen(self) -> str:
        return self.__wopen

    def __set_wopen(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Compat type must be a non-empty string")
        self.__wopen = value.strip()

    def __get_attack_power(self) -> int:
        return self.__attack

    def __set_attack_power(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Attack must be a positive integer")
        self.__attack = value

    def __get_health(self) -> int:
        return self.__health

    def __set_health(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Health must be a positive integer")
        self.__health = (
            float("inf") if self.rarity == Rarity.HAMID.value else value
        )

    attack_power = property(__get_attack_power, __set_attack_power)
    health = property(__get_health, __set_health)
    wopen = property(__get_wopen, __set_wopen)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        mana: int = int(game_state.get("mana", 0))
        if self.is_playable(mana):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite card deployed",
                "remaining_mana": mana - self.cost
            }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": None,
            "remaining_mana": mana
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.__attack_power,
            "combat_type": self.__wopen
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_taken: int = min(incoming_damage, 2)
        damage_blocked: int = incoming_damage - damage_taken
        self.__health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.__health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack": self.__attack_power,
            "health": self.__health
        }

    def cast_spell(
        self, spell_name: str, targets: List[Any]
    ) -> Dict[str, Any]:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        return {
            "channeled": amount,
            "total_mana": amount + 4
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {
            "spell_power": 10,
            "mana_efficiency": 5
        }
