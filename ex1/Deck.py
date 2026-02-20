import random
from typing import List, Dict, Any
from ex0.Card import Card


class Deck:
    """Management class for a collection of cards."""

    def __init__(self) -> None:
        self.__cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added")
        if any(c.name == card.name for c in self.__cards):
            raise ValueError(f"Card '{card.name}' already exists")
        self.__cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        target = next((c for c in self.__cards if c.name == card_name), None)
        if target:
            self.__cards.remove(target)
            return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        if not self.__cards:
            raise IndexError("Deck is empty")
        return self.__cards.pop()

    def get_deck_stats(self) -> Dict[str, Any]:
        rarities: Dict[str, int] = {}
        for card in self.__cards:
            rarities[card.rarity] = rarities.get(card.rarity, 0) + 1

        return {
            "total_cards": len(self.__cards),
            "rarity_distribution": rarities
        }
