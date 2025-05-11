from typing import Callable
from dataclasses import dataclass

import keyboard

from signals import signals

HOTKEY_MODIFIER = "ctrl"  # Модификатор горячих цифровых клавиш
KEY_BEGIN_DIALOGUE = "scroll lock"  # Клавиша вызова окна замены регистров


@dataclass
class Hotkey:  # Описание горячей клавиши
    key: str  # Горячая клавиша
    function: Callable  # Функция обработки горячей клавиши
    modifier: bool = False  # Признак, требуется ли горячей клавише модификатор


def my_signature():
    """Вывод личной подписи"""
    keyboard.write("С уважением,")
    keyboard.release(HOTKEY_MODIFIER)  # Гасим модификатор от нажатия горячей клавиши
    keyboard.send("shift+enter")
    keyboard.write("Леонид Большаков")


hotkeys = (
    Hotkey("3", lambda: keyboard.write("bolleoa@gmail.com"), modifier=True),
    Hotkey("7", lambda: keyboard.write("9025138590"), modifier=True),
    Hotkey("9", my_signature, modifier=True),
    Hotkey("caps lock", lambda: keyboard.send("alt+right shift")),
    Hotkey("scroll lock", lambda: signals.start_dialogue.emit()),
)


def set_hotkeys():
    for hotkey in hotkeys:
        key = f"{HOTKEY_MODIFIER}+{hotkey.key}" if hotkey.modifier else hotkey.key
        keyboard.add_hotkey(key, hotkey.function, suppress=True)
