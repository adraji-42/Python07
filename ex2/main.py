import inspect
from .EliteCard import EliteCard
from typing import Any, Dict, List, Tuple


def get_mro_functions(target: Any) -> Dict[str, List[Tuple[str, Any]]]:
    """Extracts functions from all classes in the Method Resolution Order.

    Args:
        target: A class or an instance to inspect.

    Returns:
        A dictionary mapping class names to their functions.
    """
    mro = target.__mro__ if inspect.isclass(target) else type(target).__mro__

    return {
        cls.__name__: inspect.getmembers(cls, predicate=inspect.isfunction)
        for cls in mro
    }


def main() -> None:

    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    for c, m in get_mro_functions(EliteCard).items():
        if c != "EliteCard" and m:
            print(f"- {c}: {[e[0] for e in m if e[0][0] != '_']}")

    card = EliteCard("Arcane Warrior", 4, "Mythic", 5, 9)

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {card.cast_spell("Fireball", ['Enemy1', 'Enemy2'])}")
    print(f"{card.channel_mana(3)}")


if __name__ == "__main__":
    main()
