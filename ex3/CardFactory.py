from ex0.Card import Card
from typing import Dict, Union, Any
from abc import ABC, abstractmethod


class CardFactory(ABC):
    """Abstract factory for creating different card types."""

    @abstractmethod
    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Creates a creature card.

        Args:
            name_or_power: Optional identifier or power level.

        Returns:
            A new creature card instance.
        """
        pass

    @abstractmethod
    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Creates a spell card.

        Args:
            name_or_power: Optional identifier or power level.

        Returns:
            A new spell card instance.
        """
        pass

    @abstractmethod
    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Creates an artifact card.

        Args:
            name_or_power: Optional identifier or power level.

        Returns:
            A new artifact card instance.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Generates a complete themed deck.

        Args:
            size: Number of cards in the deck.

        Returns:
            Dictionary containing deck details.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, Any]:
        """Lists all supported card types by this factory.

        Returns:
            Dictionary mapping type categories to lists of specific types.
        """
        pass
