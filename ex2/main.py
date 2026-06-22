import inspect
from ex0 import Rarity
from .EliteCard import EliteCard
from typing import Any, Dict, List, Tuple


def get_mro_functions(target: Any) -> Dict[str, List[Tuple[str, Any]]]:

    mro = target.__mro__ if inspect.isclass(target) else type(target).__mro__

    return {
        cls.__name__: inspect.getmembers(cls, predicate=inspect.isfunction)
        for cls in mro
    }


def main() -> None:

    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    try:
        for c, m in get_mro_functions(EliteCard).items():
            if c != "EliteCard" and m:
                print(f"- {c}: {[e[0] for e in m if e[0][0] != '_']}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    card = EliteCard("Arcane Warrior", 4, Rarity.MYTHIC.value, 5, 9, "melee")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    try:
        result = card.play(
            {"mana": 9, "damage_taken": 5}
        )
        for r in result:
            print(f"{r}: {result[r]}")
    except KeyError as e:
        print(f"Messing key: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    print("\nMagic phase:")
    try:
        result = card.play(
            {
                "combat_type": "magic", "mana": 9,
                "spell": "Fireball", "targets": ["Enemy1", "Enemy2"]
            }
        )
        for r in result:
            print(f"{r}: {result[r]}")
    except KeyError as e:
        print(f"Messing key: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError) as e:
        print(f"Instance Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
