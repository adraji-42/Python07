import random
from ex0 import Card
from .GameStrategy import GameStrategy
from .CardFactory import CardFactory
from typing import Any, Dict, List, Optional


class GameEngine:

    def __init__(self) -> None:
        self.__factory: Optional[CardFactory] = None
        self.__strategy: Optional[GameStrategy] = None
        self.__simulated_turns: int = 0
        self.__total_damage: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:

        if not isinstance(factory, CardFactory):
            raise TypeError(
                "The GameEngine uses a factory-type card CardFactory."
            )
        self.__factory = factory

        if not isinstance(strategy, GameStrategy):
            raise TypeError(
                "The GameEngine uses a strategy-type card GameStrategy."
            )
        self.__strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:

        if not self.__factory or not self.__strategy:
            raise RuntimeError("Engine lacks required configuration.")

        deck_data = self.__factory.create_themed_deck(random.randint(2, 6))
        hand: List[Card] = []
        if isinstance(deck_data.get("cards"), list):
            hand = deck_data["cards"]

        self.__simulated_turns += 1

        print("\nSimulating aggressive turn...")
        print(
            "Hand: "
            f"{
                str([
                    f"{card.name} ({card.cost})" for card in hand
                ]).replace("'", "")
            }"
        )
        print("\nTurn execution:")
        print(f"Strategy: {self.__strategy.get_strategy_name()}")

        result = self.__strategy.execute_turn(hand, [])
        self.__total_damage += result["damage_dealt"]
        return result

    def get_engine_status(self) -> Dict[str, Any]:

        return {
            'turns_simulated': self.__simulated_turns,
            'strategy_used': self.__strategy.get_strategy_name(),
            'total_damage': self.__total_damage,
            'cards_created': len(self.__factory.get_history())
        }
