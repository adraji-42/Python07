from .Card import Rarity
from .CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
    print("\nCreatureCard Info:")
    print(dragon.get_card_info())

    game_state = {
        "effect": "Creature summoned to battlefield",
        "mana": 6
    }

    try:
        print(
            f"\nPlaying {dragon.name} with "
            f"{game_state['mana']} mana available:"
        )
        print(f"Playable: {dragon.is_playable(game_state['mana'])}")
        print(f"Play result: {dragon.play(game_state)}")
    except KeyError as e:
        print(f"Error: {e} Not found")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    target = "Goblin Warrior"
    print(f"\n{dragon.name} attacks {target}:")
    print(f"Attack result: {dragon.attack_target(target)}")

    insufficient_mana = 3

    try:
        print(f"\nTesting insufficient mana ({insufficient_mana} available):")
        print(f"Playable: {dragon.is_playable(insufficient_mana)}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError) as e:
        print(f"Instance Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
