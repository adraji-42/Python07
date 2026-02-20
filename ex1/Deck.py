import random
from ex0.Card import Card
from typing import List, Dict


class Deck:
    """Class to manage a collection of cards."""

    def __init__(self) -> None:
        self.__cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added")
        if any(c.name == card.name for c in self.__cards):
            raise ValueError(f"Card '{card.name}' already exists")
        self.__cards.append(card)

    def remove_card(self, card_name: str) -> None:
        target_card = next(
            (c for c in self.__cards if c.name == card_name), None
        )
        if not target_card:
            raise ValueError(f"Card not found: '{card_name}'")
        self.__cards.remove(target_card)

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        if not self.__cards:
            raise IndexError("Deck is empty")
        return self.__cards.pop()

    def get_deck_stats(self) -> Dict[str, int]:
        stats: Dict[str, int] = {}
        for card in self.__cards:
            stats[card.rarity] = stats.get(card.rarity, 0) + 1
        return stats
