from dataclasses import dataclass
from pynput.keyboard import Key


@dataclass(frozen=True, slots=False)
class Const:
    TEXT_YES_BUTTON = "Заменить текстом 1 "
    TEXT_OK_BUTTON = "Заменить текстом 2 "
    TEXT_CANCEL_BUTTON = "Оставить прежним"
    TEXT_CRITICAL_ERROR = (
        "Ошибка в программе. функция f.init_PyQt6() вернула недопустимый код возврата -"
    )
    KEY_SCROLL_LOCK = Key.scroll_lock
    KEY_CTRL_SCROLL_LOCK = "<3>"
