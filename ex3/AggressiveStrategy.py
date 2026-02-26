from ex0 import Card, CreatureCard
from typing import Dict, List, Any
from .GameStrategy import GameStrategy
from ex1 import ArtifactCard, SpellCard
from .FantasyCardFactory import SupportedCards


class AggressiveStrategy(GameStrategy):

    def execute_turn(
        self, hand: List[Card], battlefield: List[Card]
    ) -> Dict[str, Any]:

        sorted_hand: List[Card] = []
        for cls in (CreatureCard, SpellCard, ArtifactCard):
            sorted_hand.extend(
                sorted(
                    [c for c in hand if isinstance(c, cls)],
                    key=lambda x: getattr(x, "cost", 0)
                )
            )
        cards_to_play = sorted_hand[:min(len(sorted_hand), 2)]
        targets = self.prioritize_targets(battlefield)

        played_cards = [
            getattr(c, "name", "Unknown") for c in cards_to_play
        ]
        mana_used = sum(getattr(c, "cost", 0) for c in cards_to_play)
        damage_output = sum(
            [SupportedCards.get_card_damage(c) for c in cards_to_play]
        )

        target_hit = "Enemy Player"
        if targets:
            target_hit = getattr(targets[0], "name", "Enemy Player")

        return {
            "cards_played": played_cards,
            "mana_used": mana_used,
            "targets_attacked": [target_hit],
            "damage_dealt": damage_output,
            "strategy_applied": self.get_strategy_name()
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        return available_targets[::-1]
