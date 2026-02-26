from ex0 import Card
from abc import ABC, abstractmethod
from typing import Dict, Union, Any, List


class CardFactory(ABC):

    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        pass
    create_creature = abstractmethod(create_creature)

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        pass
    create_spell = abstractmethod(create_spell)

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        pass
    create_artifact = abstractmethod(create_artifact)

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        pass
    create_themed_deck = abstractmethod(create_themed_deck)

    def get_supported_types(self) -> Dict[str, List[str]]:
        pass
    get_supported_types = abstractmethod(get_supported_types)

    def get_history(self) -> List[Card]:
        pass
    get_history = abstractmethod(get_history)
