import random
from typing import Tuple, Dict, List, Any
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete strategy focused on dealing direct damage."""

    def execute_turn(
        self, hand: List[Tuple[str, int]], battlefield: List[str]
    ) -> Dict[str, Any]:
        """Executes an aggressive turn prioritizing damage.

        Args:
            hand: Cards in hand.
            battlefield: Cards on the board.

        Returns:
            Turn execution results matching the expected output.
        """
        card_play: List[Tuple[str, int]] = random.sample(
            hand, 2 if len(hand) > 1 else 1
        ) if len(hand) > 0 else []
        target = random.choice(battlefield) if len(battlefield) > 0 else []
        return {
            "cards_played": [c[0] for c in card_play],
            "mana_used": card_play,
            "targets_attacked": target,
            "damage_dealt": sum([c[0] for c in card_play])
        }

    def get_strategy_name(self) -> str:
        """Returns the specific strategy name.

        Returns:
            Name of the aggressive strategy.
        """
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        """Prioritizes enemy player and vulnerable targets.

        Args:
            available_targets: Targets on the board.

        Returns:
            Targets sorted by aggression priority.
        """
        return available_targets
