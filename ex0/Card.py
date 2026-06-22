from enum import Enum
from abc import ABC, abstractmethod
from typing import Dict, Any, Union, Final


class Rarity(Enum):

    COMMON: Final[str] = "Common"
    UNCOMMON: Final[str] = "Uncommon"
    RARE: Final[str] = "Rare"
    EPIC: Final[str] = "Epic"
    LEGENDARY: Final[str] = "Legendary"
    MYTHIC: Final[str] = "Mythic"

    # Hamed is an abbreviation for Hybrid Anomaly of Manifested Imperial Dread
    HAMID: Final[str] = "Hamid"


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.__name: str = ""
        self.__cost: int = 0
        self.__rarity: str = ""

        self.name = name
        self.rarity = rarity
        self.cost = cost

        if self.__rarity == Rarity.HAMID.value:
            print(
                f"\n{'-' * 60}\nCongratulations, "
                f"you now own the rarest card in history.\n{'-' * 60}\n"
            )

    def __get_name(self) -> str:
        return self.__name

    def __set_name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self.__name = value.strip()

    def __get_cost(self) -> int:
        return self.__cost

    def __set_cost(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Cost must be a positive integer")
        self.__cost = 0 if self.__rarity == Rarity.HAMID.value else value

    def __get_rarity(self) -> str:
        return self.__rarity

    def __set_rarity(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Rarity must be a string")
        try:
            Rarity(value)
        except ValueError:
            raise ValueError(f"Rarity '{value}' is not valid")
        self.__rarity = value
        if self.__rarity == Rarity.HAMID.value:
            self.__cost = 0

    name = property(__get_name, __set_name)
    cost = property(__get_cost, __set_cost)
    rarity = property(__get_rarity, __set_rarity)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass
    play = abstractmethod(play)

    def get_card_info(self) -> Dict[str, Union[str, int]]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
