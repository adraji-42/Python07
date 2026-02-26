import random
from ex0 import Card
from typing import List, Dict, Any


class Deck:

    def __init__(self) -> None:
        self.__cards: List[Card] = []

    def __get_cards(self) -> List[Card]:
        return self.__cards
    cards = property(__get_cards)

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added to the deck")
        self.__cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.__cards:
            if card.name == card_name:
                self.__cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        if not self.__cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.__cards.pop()

    def get_deck_stats(self) -> Dict[str, Any]:
        creatures: int = sum(
            1 for c in self.__cards if type(c).__name__ == "CreatureCard"
        )
        spells: int = sum(
            1 for c in self.__cards if type(c).__name__ == "SpellCard"
        )
        artifacts: int = sum(
            1 for c in self.__cards if type(c).__name__ == "ArtifactCard"
        )

        avg_cost: float = 0.0
        if self.__cards:
            avg_cost = sum(c.cost for c in self.__cards) / len(self.__cards)

        return {
            "total_cards": len(self.__cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
