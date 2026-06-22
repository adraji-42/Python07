from ex2 import Combatable
from ex0 import Card, Rarity
from .Rankable import Rankable
from typing import Any, Dict


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self, name: str, cost: int, rarity: str, health: int, attack: int
    ) -> None:
        if rarity == Rarity.HAMID.value:
            rarity = Rarity.MYTHIC.value
        super().__init__(name, cost, rarity)
        self.__wins: int = 0
        self.__losses: int = 0
        self.__rating: int = 1200
        self.__health: int = 0
        self.__attack_power: int = 0
        self.attack_power = attack
        self.health = health

    def __get_attack(self) -> int:
        return self.__attack_power

    def __set_attack(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Attack must be a positive integer")
        self.__attack_power = value

    def __get_health(self) -> int:
        return self.__health

    def __set_health(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Health must be a positive integer")
        self.__health = value

    attack_power = property(__get_attack, __set_attack)
    health = property(__get_health, __set_health)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        mana: int = int(game_state.get("mana", 0))
        if self.is_playable(mana):
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Tournament play",
                "remaining_mana": mana - self.cost
            }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": None,
            "remaining_mana": mana
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.__attack_power,
            "combat_type": "tournament_melee"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        self.__health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": 0,
            "still_alive": self.__health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack": self.__attack_power,
            "health": self.__health
        }

    def calculate_rating(self) -> int:
        return 1200 + (self.__wins * 16) - (self.__losses * 16)

    def update_wins(self, wins: int) -> None:
        self.__wins += wins
        self.__rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.__losses += losses
        self.__rating = self.calculate_rating()

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            "rating": self.__rating,
            "wins": self.__wins,
            "losses": self.__losses
        }

    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "rating": self.__rating,
            "record": f"{self.__wins}-{self.__losses}"
        }
