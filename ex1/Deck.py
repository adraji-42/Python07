import random
from ex0 import Card
from typing import List, Optional


class Deck:
    """A class to manage a collection of cards.

    Attributes:
        __cards: Private list to store Card objects.
    """

    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        self.__cards: List[Card] = []
        if cards:
            for card in cards:
                try:
                    self.add_card(card)
                except Exception as e:
                    print(f"Error {e}")

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added to the deck")
        if any(c.name == card.name for c in self.__cards):
            raise ValueError(f"Card with name '{card.name}' already exists")
        self.__cards.append(card)

    def remove_card(self, card_name: str) -> None:
        target = next((c for c in self.__cards if c.name == card_name), None)
        if not target:
            raise ValueError(f"Card '{card_name}' not found in deck")
        self.__cards.remove(target)

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        if not self.__cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.__cards.pop()

    def get_deck_size(self) -> int:
        return len(self.__cards)

    def get_cards_by_rarity(self, rarity: str) -> List[Card]:
        return [c for c in self.__cards if c.rarity == rarity.capitalize()]
