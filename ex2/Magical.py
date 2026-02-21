from typing import Any, Dict, List
from abc import ABC, abstractmethod


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[Any, Any]:
        pass
