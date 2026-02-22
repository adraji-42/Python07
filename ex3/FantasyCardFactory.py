from ex0.Card import Card
from ex1.SpellCard import SpellCard
from typing import Dict, List
from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """Concrete factory implementation for fantasy-themed cards."""

    def __init__(self):
        self.__cards: List[Card] = []

    def create_creature(
        self, name, cost: int, rarity: str, attack: int, health: int
    ) -> Card:
        """Creates a customized fantasy creature card.

        Args:
            name: The name of the creature.
            cost: The mana cost.
            rarity: The rarity level.
            attack: The attack power.
            health: The health points.

        Returns:
            A customized CreatureCard instance.
        """
        self.__cards.append(CreatureCard(name, cost, rarity, attack, health))
        return self.__cards[-1]

    def create_spell(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> Card:
        """Creates a customized fantasy spell card.

        Args:
            name: The name of the spell.
            cost: The mana cost.
            rarity: The rarity level.
            effect_type: The type of magical effect.

        Returns:
            A customized SpellCard instance.
        """
        self.__cards.append(SpellCard(name, cost, rarity, effect_type))
        return self.__cards[-1]

    def create_artifact(
        self, name: str, cost: int, rarity: str, durability: int, ability: str
    ) -> Card:
        """Creates a customized fantasy artifact card.

        Args:
            name: The name of the artifact.
            cost: The mana cost.
            rarity: The rarity level.
            durability: The durability of the item.
            ability: The special ability name.

        Returns:
            A customized ArtifactCard instance.
        """
        self.__cards.append(
            ArtifactCard(name, cost, rarity, durability, ability)
        )
        return self.__cards[-1]

    def get_supported_types(self) -> Dict[str, List[str]]:
        """Lists supported fantasy elements.

        Returns:
            Dictionary of supported fantasy card subtypes.
        """
        return {
            "creatures": ["dragon", "goblin", "orc"],
            "spells": ["fireball", "heal", "freeze"],
            "artifacts": ["mana_ring", "shield", "staff"]
        }
