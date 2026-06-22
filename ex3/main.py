from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main() -> None:

    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    try:
        actions = engine.simulate_turn()
        print(f"Actions: {actions}")
    except (TypeError, ValueError) as e:
        print(f"Instance Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    try:
        main()
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
