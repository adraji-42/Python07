from .Deck import Deck
from ex0 import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


def main() -> None:

    print("\n=== DataDeck Deck Builder ===")

    deck = Deck()
    cards = {
        CreatureCard(
            "Fire Dragon", 5, "Epic", 7, 9
        ): {"effect": "Creature summoned to battlefield"},
        ArtifactCard(
            "Mana Crystal", 2, "Mythic", 9, "Permanent: +1 mana per turn"
        ): {
            "artifact_slots": 3, "mana": 9, "effect": "Deal 3 damage to target"
        },
        SpellCard(
            "Lightning Bolt", 3, "Uncommon", "Electric"
        ): {"mana": 9, "effect": "Deal 3 damage to target"}
    }

    print("\nBuilding deck with different card types...")

    for card in cards:
        try:
            deck.add_card(card)
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    deck_stats = deck.get_deck_stats()
    print(f"\nDeck stats: {deck_stats}")

    print("\nDrawing and playing cards:")
    for _ in range(deck_stats['total_cards']):
        card = deck.draw_card()
        c_type = card.__class__.__name__.removesuffix('Card')

        print(f"\nDrew: {card.name} ({c_type})")
        print(f"Play result: {card.play(cards[card])}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
