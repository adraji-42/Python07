from abc import ABC, abstractmethod
from typing import Dict, List, Any


class GameStrategy(ABC):
    """Abstract interface defining a game strategy."""

    @abstractmethod
    def execute_turn(
        self, hand: List[Any], battlefield: List[Any]
    ) -> Dict[str, Any]:
        """Executes a turn based on the strategy.

        Args:
            hand: The current cards in the player's hand.
            battlefield: The current cards on the board.

        Returns:
            Dictionary containing turn execution details.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Retrieves the name of the strategy.

        Returns:
            The strategy name.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Sorts available targets by priority.

        Args:
            available_targets: Targets that can be attacked or affected.

        Returns:
            List of prioritized targets.
        """
        pass
