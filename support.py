import keyboard

9


# Для определения кода клавиши. Запустите программу и нажмите нужную клавишу - программа выведет код клавиши.
# Например, для Windows,
# при нажатии на scr_lk будет выведено "Key.scroll_lock",
# Этот текст можно будет вставить в const.py. Key.scroll_lock.


def on_press(event: keyboard._keyboard_event.KeyboardEvent) -> None:
    print(f"{event.name=} {event.scan_code=} {event.event_type=} {event.modifiers=}")


keyboard.add_hotkey("ctrl+4", lambda: keyboard.write("Мы здесь"))

keyboard.on_release(on_press)
keyboard.wait("esc")

# Уберите комментарии у следующих операторов.
# Выполнив программу Вы получите словарь замены символов в формате json.
# Далее в методе __init__ класса ReplaceText модуля replacetext.py можно вставить аналогичные операторы для чтения.
# В начале модуля надо будет убрать строчку from symbols import en_to_ru

# import json
# with open(file="config.json", mode="w") as f:
#     json.dump(en_to_ru, f)
