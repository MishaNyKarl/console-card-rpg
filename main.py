from tools import get_choice

from player import Player
from player import RACES_NAMES, RACES_MODIFIERS

from cards import LootCard, EnemyCard, print_cards_row


class Game:
    def __init__(self):
        self.player = None
        self.enemy_deck = []
        self.loot_deck = []

    def start(self):
        start_menu_options = {1: "Новая игра", 2: "Загрузить игру"}
        start_choice = get_choice("Выбери действие, герой: ", start_menu_options)
        if start_choice == 1:
            self.new_game()
        else:
            self.load_game()

    def new_game(self):
        name_choice = input("Введи имя, герой: ")

        race_list = list(RACES_NAMES.keys())
        race_options = dict()
        for i, race in enumerate(RACES_NAMES, start=1):
            race_options.setdefault(i, RACES_NAMES.get(race))

        race_choice = get_choice(f"Выбери расу, {name_choice}: ", race_options)

        self.player = Player(name_choice, race_list[race_choice])
        self.start_game()

    def start_game(self):
        self.generate_starting_cards()

        print("\nВыбираем карты лута:")
        selected_loot_cards = self.choose_cards(self.starting_loot_cards)
        self.player.add_to_loot_deck(selected_loot_cards)
        print('Ваша колода карт с лутом:')
        print_cards_row(self.player.loot_deck, 4)

        print("\nВыбираем карты врагов:")
        selected_enemy_cards = self.choose_cards(self.starting_enemy_cards)
        self.player.add_to_enemy_deck(selected_enemy_cards)
        print('Ваша колода карт со врагами:')
        print_cards_row(self.player.loot_deck, 4)

        print(self.player)

    def generate_starting_cards(self):
        self.starting_loot_cards = [
            LootCard("Кинжал", "Добавляет +2 к атаке", "weapon", 2),
            LootCard("Щит", "Добавляет +1 к броне", "armor", 1),
            LootCard("Эликсир силы", "Временно +3 к атаке", "elixir", 3, duration=2),
            LootCard("Шлем", "Добавляет +1 к броне", "armor", 1),
            LootCard("Эликсир маны", "Временно +5 маны", "elixir", 5, duration=1),
        ]

        self.starting_enemy_cards = [
            EnemyCard("Гоблин", "Слабый, но быстрый", 5, 0, 1),
            EnemyCard("Орк", "Сильный, но медленный", 8, 1, 2),
            EnemyCard("Разбойник", "Средний урон", 6, 2, 2),
            EnemyCard("Маг", "Атакует магией", 4, 0, 3),
            EnemyCard("Волк", "Быстрый укус", 5, 0, 1),
        ]

    def choose_cards(self, cards, count=3):
        print_cards_row(cards, 3)
        selected_cards = []
        cards_choice_str = input(f'Выберите {count} карт, введя их номера через пробел: ').split(' ')
        # TODO: Реализовать проверку на легитимность ввода (реализовать функцию для обработки сценария выбора карт)
        for card_index in cards_choice_str:
            selected_cards.append(cards[int(card_index) - 1])
        return selected_cards

    def game_loop(self):
        print(f"Игра началась!")


if __name__ == "__main__":
    game = Game()
    # game.start_game() # Для теста

    game.start()


