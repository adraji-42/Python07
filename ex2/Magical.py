from typing import Dict, Any, List
from abc import ABC, abstractmethod


class Magical(ABC):

    def cast_spell(
        self, spell_name: str, targets: List[Any]
    ) -> Dict[str, Any]:
        pass
    cast_spell = abstractmethod(cast_spell)

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        pass
    channel_mana = abstractmethod(channel_mana)

    def get_magic_stats(self) -> Dict[str, Any]:
        pass
    get_magic_stats = abstractmethod(get_magic_stats)
