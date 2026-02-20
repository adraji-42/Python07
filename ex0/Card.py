from typing import Any, Dict, List
from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract Base Class for all cards in DataDeck."""

    valid_rarities: List[str] = [
        "Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic", "Hamid"
    ]

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.__name: str = "Card"
        self.__cost: int = 0
        self.__rarity: str = "Stupid"

        self.name = name
        self.rarity = rarity
        self.cost = cost

        if self.__rarity == "Hamid":
            print(
                f"\n{'-' * 60}\nCongratulations, "
                f"you now own the rarest card in history.\n{'-' * 60}\n"
            )

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self.__name = name.strip()

    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int) -> None:
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Cost must be a positive integer")
        self.__cost = 0 if self.rarity == "Hamid" else cost

    @property
    def rarity(self) -> str:
        return self.__rarity

    @rarity.setter
    def rarity(self, rarity: str) -> None:
        if not isinstance(rarity, str):
            raise TypeError("Rarity must be a string")
        clean_rarity = rarity.strip().capitalize()
        if clean_rarity not in self.valid_rarities:
            raise ValueError(f"Invalid rarity: '{clean_rarity}'")

        self.__rarity = clean_rarity
        if self.__rarity == "Hamid":
            self.__cost = 0

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
