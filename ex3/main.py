from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


def main() -> None:
    """Executes the demonstration for Exercise 3."""
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    hand = [
        ("Fire Dragon", 5), ("Goblin Warrior", 2), ("Lightning Bolt", 3)
    ]

    print("\nSimulating aggressive turn...")
    print(str([f"{c[0]} ({c[1]})" for c in hand]).replace("'", ""))

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    actions = engine.simulate_turn()
    print(f"Actions: {actions}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
