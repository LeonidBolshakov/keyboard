from typing import Callable
from dataclasses import dataclass

import keyboard

from signals import signals
from const import Const as C


@dataclass
class Hotkey:  # Описание горячей клавиши
    key: str  # Горячая клавиша
    function: Callable  # Функция обработки горячей клавиши
    modifier: bool = False  # Признак, требуется ли горячей клавише модификатор


def my_signature():
    """Вывод личной подписи"""
    keyboard.write(C.TEXT_SIGN1)
    keyboard.release(C.HOTKEY_MODIFIER)  # Гасим модификатор от нажатия горячей клавиши
    keyboard.send(C.KEY_SIGN2)
    keyboard.write(C.TEXT_SIGN3)


hotkeys = (
    Hotkey(C.HOTKEY_MAIL, lambda: keyboard.write(C.TEXT_WRITE_MAIL), modifier=True),
    Hotkey(C.HOTKEY_TEL, lambda: keyboard.write(C.TEXT_WRITE_TEL), modifier=True),
    Hotkey(C.HOTKEY_MY_SIGNATURE, my_signature, modifier=True),
    Hotkey(C.HOTKEY_CHANGE_REGISTER, lambda: keyboard.send(C.KEY_CHANGE_REGISTER)),
    Hotkey(C.HOTKEY_BEGIN_DIALOGUE, lambda: signals.start_dialogue.emit()),
)


def set_hotkeys():
    for hotkey in hotkeys:
        key = f"{C.HOTKEY_MODIFIER}+{hotkey.key}" if hotkey.modifier else hotkey.key
        keyboard.add_hotkey(key, hotkey.function, suppress=True)
