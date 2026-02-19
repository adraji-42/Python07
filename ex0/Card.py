from typing import Any, Dict
from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract Base Class for all cards in DataDeck.

    Attributes:
        name: The name of the card.
        cost: The mana cost required to play the card.
        rarity: The rarity level of the card.
    """
    valid_rarities = [
        "Common", "Uncommon", "Rare", "Legendary", "Mythic", "Hamid"
    ]

    def __init__(self, name: str, cost: int, rarity: str) -> None:

        self.__name: str = "Card"
        self.__cost: int = 0
        self.__rarity: str = "stupid"

        assert isinstance(name, str), "Name must be a string"
        clean_name: str = name.strip().capitalize()
        assert clean_name, "The card name cannot be empty or white spaces"
        self.__name: str = clean_name

        assert isinstance(cost, int), "The cost of card must be integer"
        assert cost >= 0, "The cost of card must be positive"
        self.__cost: int = cost

        assert isinstance(rarity, str), "Rarity must be a string"
        clean_rarity: str = rarity.strip().capitalize()

        assert clean_rarity in self.valid_rarities, (
            "The rarity should be one of these "
            f"{[r for r in self.valid_rarities if r != "Hamid"]}"
        )
        self.__rarity: str = clean_rarity
        if clean_rarity == "Hamid":
            print(
                f"\n{'-' * 60}\nCongratulations, "
                f"you now own the rarest card in history.\n{'-' * 60}\n"
            )
            self.__cost = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> str:
        assert isinstance(name, str), "Name must be a string"
        clean_name: str = name.strip().capitalize()
        assert clean_name, "The card name cannot be empty or white spaces"
        self.__name: str = clean_name

    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int) -> int:
        assert isinstance(cost, int), "The cost of card must be integer"
        assert cost >= 0, "The cost of card must be positive"
        self.__cost: int = cost

    @property
    def rarity(self) -> str:
        return self.__rarity

    @rarity.setter
    def rarity(self, rarity: str) -> str:
        assert isinstance(rarity, str), "Rarity must be a string"
        clean_rarity: str = rarity.strip().capitalize()

        assert clean_rarity in self.valid_rarities, (
            "The rarity should be one of these "
            f"{[r for r in self.valid_rarities if r != "Hamid"]}"
        )
        if clean_rarity == "Hamid" and self.__rarity != "Hamid":
            print(
                f"\n{'-' * 60}\nCongratulations, "
                f"you now own the rarest card in history.\n{'-' * 60}\n"
            )
            self.__cost = 0
        self.__rarity: str = clean_rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def get_card_info(self) -> Dict[str, Any]:
        return {
            "name": self.__name,
            "cost": self.__cost,
            "rarity": self.__rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.__cost
