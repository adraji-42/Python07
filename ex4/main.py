import inspect
from ex0 import Rarity
from typing import Type, List
from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def get_interfaces(cls: Type) -> List[str]:
    if not inspect.isclass(cls):
        cls = cls.__class__

    interfaces = [
        base.__name__ for base in cls.__mro__
        if inspect.isabstract(base) and base is not cls
    ]
    return interfaces


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")

    card1 = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 10, 50)
    card2 = TournamentCard("Ice Wizard", 3, Rarity.EPIC.value, 5, 100)

    try:
        id1 = platform.register_card(card1)

        print(f"\n{card1.name} (ID: {id1}):")
        print(f"Interfaces: {str(get_interfaces(card1)).replace("'", "")}")
        print(f"Rating: {card1.get_rank_info()['rating']}")
        print(f"Record: {card1.get_tournament_stats()['record']}")
    except TypeError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")

    try:
        id2 = platform.register_card(card2)

        print(f"\n{card2.name} (ID: {id2}):")
        print(f"Interfaces: {str(get_interfaces(card2)).replace("'", "")}")
        print(f"Rating: {card2.get_rank_info()['rating']}")
        print(f"Record: {card2.get_tournament_stats()['record']}")
    except TypeError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")

    print("\nCreating tournament match...")
    try:
        match_result = platform.create_match(id1, id2)
    except KeyError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")

    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, stats in enumerate(leaderboard, 1):
        print(f"{i}. {stats['name']}")
        print(f"Rating: {stats['rating']} ({stats['record']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
