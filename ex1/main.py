from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


def main() -> None:
    print("=== DataDeck: Exercise 1 - Advanced Game State Test ===")

    fireball = SpellCard("Fireball", 3, "Rare", "Fire Damage")

    state = {
        "mana": 10,
        "targets": ["Enemy Goblin", "Enemy Orc"],
        "artifacts_on_field": 1
    }

    print(f"\nPlaying {fireball.name}:")
    print(fireball.play(state))

    shield = ArtifactCard("Mystic Shield", 2, "Common", 3, "Absorb Damage")
    print(f"\nPlaying {shield.name}:")
    print(shield.play(state))

    print("\nActivating Artifact Ability:")
    print(shield.activate_ability())
    print(f"New Durability: {shield.durability}")


if __name__ == "__main__":
    main()
