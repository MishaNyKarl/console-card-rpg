from typing import Optional
from tools import wrap_text, center_text

LOOT_CARD_TYPES_NAMES = {
    'weapon': 'Оружие',
    'armor': 'Броня',
    'elixir': 'Эликсир'
}
EFFECT_TYPES_NAMES = {
    'damage': 'урон',
    'heal': 'восстановление'
}
CARD_WIDTH = 30


def print_cards_row(cards, num_in_row=None):
    """
    Принимает список карт, печатает их в несколько рядов (по num_in_row карт в ряду), нумеруя их.
    Если num_in_row не указан, выводит все карты в одном ряду.
    """
    if num_in_row is None:
        num_in_row = len(cards)

    card_chunks = [cards[i:i + num_in_row] for i in range(0, len(cards), num_in_row)]
    global_index = 1

    for chunk in card_chunks:
        card_strs = [str(card).split('\n') for card in chunk]
        max_lines = max(len(lines) for lines in card_strs)

        for lines in card_strs:
            while len(lines) < max_lines:
                lines.append(" " * len(lines[0]))

        index_line = []
        for i in range(len(chunk)):
            card_width = len(card_strs[i][0])
            label = f"[{global_index + i}]"
            index = label.ljust(card_width)
            index_line.append(index)
        print("  ".join(index_line))

        for line_parts in zip(*card_strs):
            print("  ".join(line_parts))
        print()
        global_index += len(chunk)
        

class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class EnemyCard(Card):
    def __init__(self, name, description, hp, armor, damage):
        super().__init__(name, description)
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def __str__(self):
        top_line = "┌" + "─" * CARD_WIDTH + "┐"
        bottom_line = "└" + "─" * CARD_WIDTH + "┘"
        border_line = f"│{center_text('_____', CARD_WIDTH)}│"

        name_line = f"│{center_text(f'{self.name}', CARD_WIDTH)}│"

        desc_lines = wrap_text(self.description, CARD_WIDTH)
        desc_block = [f"│ {line}" + " " * (CARD_WIDTH + 1 - len(line) - 2) + "│" for line in desc_lines]

        hp_value = f"│ Жизни: {self.hp}"
        hp_line = hp_value + " " * (CARD_WIDTH - len(hp_value) + 1) + "│"
        armor_value = f"│ Броня: {self.armor}"
        armor_line = armor_value + " " * (CARD_WIDTH - len(armor_value) + 1) + "│"
        damage_value = f"│ Урон: {self.damage}"
        damage_line = damage_value + " " * (CARD_WIDTH - len(damage_value) + 1) + "│"

        return "\n".join(
            [top_line, name_line, border_line] + desc_block + [border_line, hp_line, armor_line, damage_line, bottom_line])


class LootCard(Card):
    def __init__(self, name, description, loot_type, value, effect=None, duration=None):
        super().__init__(name, description)
        self.loot_type = loot_type
        self.value = value
        self.duration = duration
        self.effect = effect

    def __str__(self):
        top_line = "┌" + "─" * CARD_WIDTH + "┐"
        bottom_line = "└" + "─" * CARD_WIDTH + "┘"
        border_line = f"│{center_text('_____', CARD_WIDTH)}│"

        name_line = f"│{center_text(f'{self.name} ({LOOT_CARD_TYPES_NAMES.get(self.loot_type)})', CARD_WIDTH)}│"

        desc_lines = wrap_text(self.description, CARD_WIDTH)
        desc_block = [f"│ {line}" + " " * (CARD_WIDTH + 1 - len(line) - 2) + "│" for line in desc_lines]

        match self.loot_type:
            case 'armor':
                value_line = f"│ Броня: {self.value}"
            case 'weapon':
                value_line = f"│ Урон: {self.value}"
            case 'elixir':
                value_line = f"│ Эффект: {self.value} {EFFECT_TYPES_NAMES.get(self.effect, 'Unknown')}"
            case _:
                value_line = f"│"

        value_line += " " * (CARD_WIDTH + 1 - len(value_line)) + "│"

        if self.duration:
            duration_line = f"│ Длительность: {self.duration} ходов"
            duration_line += " " * (CARD_WIDTH + 1 - len(duration_line)) + "│"
        else:
            duration_line = f"│ Длительность: перманентно"
            duration_line += " " * (CARD_WIDTH + 1 - len(duration_line)) + "│"

        return "\n".join([top_line, name_line, border_line] + desc_block + [border_line, value_line, duration_line, bottom_line])
