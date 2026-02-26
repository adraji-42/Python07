import random
from sys import exit
from enum import Enum
from .CardFactory import CardFactory
from ex0 import Card, CreatureCard, Rarity
from ex1 import SpellCard, ArtifactCard, Deck
from typing import Dict, List, Tuple, Union, Final, Callable


class SupportedCards(Enum):

    CREATURE = ("Dragon", "Goblin", "Orc")
    SPELL = ("Fireball", "Heal", "Freeze")
    ARTIFACT = ("Mana Ring", "Shield", "Wand")

    def get_card_damage(card: Card) -> int:
        if isinstance(card, CreatureCard):
            return SupportedCreatureCard.get_creature_damage(card)
        if isinstance(card, SpellCard):
            return SupportedSpellCards.get_spell_damage(card)
        if isinstance(card, ArtifactCard):
            return SupportedArtifactCard.get_artifact_damage(card)
    get_card_damage = staticmethod(get_card_damage)


class SupportedCreatureCard(Enum):

    DRAGON: Final[Tuple[str, int, Rarity, int, int]] = (
        "Dragon", 100,
        (
            Rarity.MYTHIC.value
            if random.randint(1, 1000) != 1 else Rarity.HAMID.value
        ),
        50, 500
    )
    GOBLIN: Final[Tuple[str, int, Rarity, int, int]] = (
        "Goblin", 10, Rarity.UNCOMMON.value, 15, 60
    )
    ORC: Final[Tuple[str, int, Rarity, int, int]] = (
        "Orc", 30, Rarity.RARE.value, 40, 180
    )

    def get_creature_damage(creature: CreatureCard) -> int:
        return creature.attack
    get_creature_damage = staticmethod(get_creature_damage)


class SupportedSpellCards(Enum):

    HEAL: Tuple[str, int, Rarity, str] = (
        "Heal", 25, Rarity.EPIC.value, "heal"
    )
    FIREBALL: Tuple[str, int, Rarity, str] = (
        "Fireball", 30, Rarity.LEGENDARY.value, "Burn"
    )
    FREEZE: Tuple[str, int, Rarity, str] = (
        "Freeze", 15, Rarity.UNCOMMON.value, "freezing&slowness"
    )

    def get_spell_damage(spell: SpellCard) -> int:
        if "Heal" == spell.name:
            return -10
        if "Fireball" == spell.name:
            return 15
        if "Freeze" == spell.name:
            return 5
        return 0
    get_spell_damage = staticmethod(get_spell_damage)


class SupportedArtifactCard(Enum):

    STAFF: Final[Tuple[str, int, Rarity, int, str]] = (
        "Staff", 25,
        (
            Rarity.LEGENDARY.value
            if random.randint(1, 1000) != 1 else Rarity.HAMID.value
        ),
        100, "Random Effect"
    )
    SHIELD: Final[Tuple[str, int, Rarity, int, str]] = (
        "Shield", 50, Rarity.MYTHIC.value, 10, "Immune damage for 3s"
    )
    MANA_RING: Final[Tuple[str, int, Rarity, int, str]] = (
        "Mana Ring", 0, Rarity.EPIC.value, 1, "Mana recharge"
    )

    def get_artifact_damage(artifact: ArtifactCard) -> Union[int, float]:

        if "Shield" in artifact.name:
            return float('inf')
        if "Mana Ring" in artifact.name:
            return -3
        if "Staff" in artifact.name:
            spells: List[SupportedSpellCards] = [
                SupportedSpellCards.HEAL,
                SupportedSpellCards.FIREBALL,
                SupportedSpellCards.FREEZE
            ]
            random_spell: SupportedSpellCards = random.choice(spells)
            return SupportedSpellCards.get_spell_damage(random_spell)
        return 0
    get_artifact_damage = staticmethod(get_artifact_damage)


class FantasyCardFactory(CardFactory):

    def __init__(self) -> None:

        self.__history: List[Card] = []

    def create_creature(
        self, creature_name: Union[str, None] = None
    ) -> Card:

        name = str(creature_name).strip().capitalize()
        if name not in SupportedCards.CREATURE.value:
            features = random.choice([c for c in SupportedCreatureCard]).value
        else:
            for creature in SupportedCreatureCard:
                if name == creature[0]:
                    features = creature
                    break

        self.__history.append(CreatureCard(*features))
        return self.__history[-1]

    def create_spell(
        self, spell_name: Union[str, None] = None
    ) -> Card:

        name = str(spell_name).strip().capitalize()
        if name not in SupportedCards.SPELL.value:
            features = random.choice([c for c in SupportedSpellCards]).value
        else:
            for spell in SupportedSpellCards:
                if name == spell[0]:
                    features = spell
                    break

        self.__history.append(SpellCard(*features))
        return self.__history[-1]

    def create_artifact(
        self, articat_name: Union[str, None] = None
    ) -> Card:

        name = str(articat_name).strip().capitalize()
        if name not in SupportedCards.ARTIFACT.value:
            features = random.choice([c for c in SupportedArtifactCard]).value
        else:
            for artifact in SupportedArtifactCard:
                if name == artifact[0]:
                    features = artifact
                    break

        self.__history.append(ArtifactCard(*features))
        return self.__history[-1]

    def create_themed_deck(
        self, size: int
    ) -> Dict[str, Union[str, int, List[Card]]]:

        deck = Deck()
        creators: List[Callable] = [
            self.create_creature,
            self.create_artifact,
            self.create_spell
        ]

        for _ in range(size):
            creator = random.choice(creators)
            deck.add_card(creator(None))
            if deck.cards[-1].rarity == Rarity.HAMID.value:
                print(
                    "GG Bro! You won! Because you have the strongest "
                    f"and rarest card ({deck.cards[-1].name}), my friend."
                )
                exit(0)

        return {
            "theme": "Random Fantasy",
            "size": size,
            "cards": deck.cards
        }

    def get_supported_types(self) -> Dict[str, List[str]]:

        return {
            "creatures": list(SupportedCards.CREATURE.value),
            "spells": list(SupportedCards.SPELL.value),
            "artifacts": list(SupportedCards.ARTIFACT.value)
        }

    def get_history(self) -> List[Card]:

        return self.__history
