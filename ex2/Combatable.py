from typing import Any, Dict
from abc import ABC, abstractmethod


class Combatable(ABC):

    def attack(self, target: Any) -> Dict[str, Any]:
        pass
    attack = abstractmethod(attack)

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        pass
    defend = abstractmethod(defend)

    def get_combat_stats(self) -> Dict[str, Any]:
        pass
    get_combat_stats = abstractmethod(get_combat_stats)
