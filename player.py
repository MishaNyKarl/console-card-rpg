BASE_STATS = {
    "hp": 10,
    "mana": 10,
    "base_damage": 1,
    "armor": 0,
}

RACES_NAMES = {
    "human": 'Человек',
    "goblin": 'Гоблин',
    "orc": 'Орк'
}

RACES_MODIFIERS = {
    "human": {
        "hp": 0,
        "mana": 0,
        "base_damage": 0,
        "armor": 0,
    },
    "goblin": {
        "hp": -2,
        "mana": +3,
        "base_damage": 0,
        "armor": 0,
    },
    "orc": {
        "hp": +5,
        "mana": -3,
        "base_damage": +1,
        "armor": +1,
    },
}


class Player:
    MAX_WEAPONS = 2
    MAX_ARMORS = 3

    def __init__(self, name, race, loot_deck=None, enemy_deck=None,):
        self.name = name
        self.race = race

        stats = BASE_STATS.copy()

        mods = RACES_MODIFIERS.get(race, {})
        for key, value in mods.items():
            stats[key] += value

        self.hp = stats["hp"]
        self.mana = stats["mana"]
        self.base_damage = stats["base_damage"]
        self.armor = stats["armor"]

        self.loot_deck = loot_deck if loot_deck else []
        self.enemy_deck = enemy_deck if enemy_deck else []

        self.equipment = {
            "weapon": [None] * self.MAX_WEAPONS,
            "armor": [None] * self.MAX_ARMORS,
        }

        self.level = 1

    def __str__(self):
        equipped_count = sum(
            1 for item in (self.equipment["weapon"] + self.equipment["armor"]) if item is not None
        )
        return(f"{self.name} [{self.race}] | "
               f"Lvl {self.level} | "
               f"HP: {self.hp} | Mana: {self.mana} | "
               f"DMG: {self.base_damage} | Armor: {self.armor} | "
               f"Loot Deck: {len(self.loot_deck)} | Enemy Deck: {len(self.enemy_deck)} | "
               f"Equipment: {equipped_count}")

    def _put_cards(self, cards, deck):
        deck.extend(cards)
        return len(deck)

    def add_to_loot_deck(self, cards) -> int:
        return self._put_cards(cards, self.loot_deck)

    def add_to_enemy_deck(self, cards) -> int:
        return self._put_cards(cards, self.enemy_deck)

    def equip_item(self, item):
        if item.loot_type == "weapon":
            for i in range(self.MAX_WEAPONS):
                if self.equipment["weapon"][i] is None:
                    self.equipment["weapon"][i] = item
                    return True
            print("Оба слота оружия заняты!")
            return False

        elif item.loot_type == "armor":
            for i in range(self.MAX_ARMORS):
                if self.equipment["armor"][i] is None:
                    self.equipment["armor"][i] = item
                    return True
            print("Все слоты брони заняты!")
            return False

        return False

    def get_loot_deck(self):
        return self.loot_deck

    def get_enemy_deck(self):
        return self.enemy_deck

    def get_equipment(self):
        return self.equipment
