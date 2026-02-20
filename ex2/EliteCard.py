from ex0 import Card
from .Magical import Magical
from typing import Dict, List
from .Combatable import Combatable


class EliteCard (Card, Combatable, Magical):

    def play(self, game_state: Dict) -> Dict:
        pass

    def attack(self, target) -> Dict:
        pass

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        pass

    def defend(self, incoming_damage: int) -> Dict:
        pass

    def get_combat_stats(self) -> Dict:
        pass

    def channel_mana(self, amount: int) -> Dict:
        pass

    def get_magic_stats(self) -> Dict:
        pass
