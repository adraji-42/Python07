import random
from enum import Enum
from typing import Dict, Any, List
from .TournamentCard import TournamentCard


class MatchResult(Enum):
    WIN = "win"
    LOSS = "loss"


class TournamentPlatform:

    def __init__(self) -> None:
        self.__cards: Dict[str, TournamentCard] = {}
        self.__matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError("Only the TournamentCard is allowed.")

        card_id: str = (
            f"{card.name.lower().replace(' ', '_')}_{len(self.__cards) + 1:03}"
        )
        self.__cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        self.__matches_played += 1
        try:
            card1: TournamentCard = self.__cards[card1_id]
            card2: TournamentCard = self.__cards[card2_id]
        except KeyError as e:
            raise ValueError(f"Unknown card id: {e}")

        result: Dict[str, Any] = {}
        score = random.choice(list(MatchResult))

        if score == MatchResult.WIN:
            card1.update_wins(1)
            card2.update_losses(1)
            result.update({"winner": card1_id, "loser": card2_id})
        elif score == MatchResult.LOSS:
            card2.update_wins(1)
            card1.update_losses(1)
            result.update({"winner": card2_id, "loser": card1_id})

        winner_card: TournamentCard = self.__cards[result["winner"]]
        loser_card: TournamentCard = self.__cards[result["loser"]]

        result.update({
            "winner_rating": winner_card.calculate_rating(),
            "loser_rating": loser_card.calculate_rating(),
        })

        return result

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        sorted_cards = sorted(
            self.__cards.values(),
            key=lambda c: c.calculate_rating(),
            reverse=True
        )
        return [card.get_tournament_stats() for card in sorted_cards]

    def generate_tournament_report(self) -> Dict[str, Any]:
        total_rating: int = sum(
            c.calculate_rating() for c in self.__cards.values()
        )
        avg_rating: float = (
            total_rating / len(self.__cards) if self.__cards else 0.0
        )

        return {
            "total_cards": len(self.__cards),
            "matches_played": self.__matches_played,
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }
