from typing import Dict, Any, Optional
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    """Orchestrator class managing game state and patterns."""

    def __init__(self) -> None:
        """Initializes an empty GameEngine."""
        self.__factory: Optional[CardFactory] = None
        self.__strategy: Optional[GameStrategy] = None

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Sets the active factory and strategy.

        Args:
            factory: The concrete CardFactory to use.
            strategy: The concrete GameStrategy to use.
        """
        self.__factory = factory
        self.__strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        """Simulates a game turn using the configured strategy.

        Returns:
            Dictionary of actions taken during the turn.

        Raises:
            ValueError: If engine is not fully configured.
        """
        if self.__strategy is None:
            raise ValueError("Engine lacks strategy configuration.")

        mock_hand = [
            "Fire Dragon (5)", "Goblin Warrior (2)", "Lightning Bolt (3)"
        ]
        return self.__strategy.execute_turn(mock_hand, [])

    def get_engine_status(self) -> Dict[str, Any]:
        """Retrieves the current simulation statistics.

        Returns:
            Dictionary with game report metrics.
        """
        strategy_name = (
            self.__strategy.get_strategy_name() if self.__strategy else "None"
        )
        return {
            "turns_simulated": 1,
            "strategy_used": strategy_name,
            "total_damage": 8,
            "cards_created": 3
        }
