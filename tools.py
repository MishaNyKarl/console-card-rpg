
def get_choice(prompt, options):
    """
    Показывает сообщение и возвращает корректный выбор пользователя.
    options — dict с индексами опций в качестве ключа и описанием в качестве значения
    """
    SIZE_OF_UNDERLINING = 30
    sent_message = "_" * SIZE_OF_UNDERLINING
    for index in options:
        sent_message += f"\n{index}. {options.get(index, 0)}"
    print(sent_message)
    while True:
        choice = input(prompt)
        if choice.isdigit():
            if int(choice) in options:
                print("_" * SIZE_OF_UNDERLINING)
                return int(choice)
            print('Такой опции нет( Введи корректное значение')


def center_text(text: str, width: int) -> str:
    """
    Центрирует текст по заданной ширине.
    Если текст длиннее ширины — обрезает.
    """
    if len(text) >= width:
        return text[:width]

    total_spaces = width - len(text)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    return " " * left_spaces + text + " " * right_spaces


def wrap_text(text, width):
    """Разбиваем описание на строки, чтобы не выходило за рамку"""
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= width:
            line += (word + " ")
        else:
            lines.append(line.rstrip())
            line = word + " "
    if line:
        lines.append(line.rstrip())
    return lines