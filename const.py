from dataclasses import dataclass
from pynput.keyboard import Key


@dataclass(frozen=True, slots=False)
class Const:
    TEXT_YES_BUTTON = "Заменить\nНажми 1"
    QSS_REPLACEMENT = "color: blue;"
    QSS_BUTTON = "font-weight: bold; font-size: 12pt; "
    TEXT_NO_BUTTON = "Не заменять\nНажми 2/Esc"
    QSS_NO_REPLACEMENT = "color: darkblue;"
    TEXT_CANCEL_BUTTON = "Выгрузить программу\nНажми 3"
    TEXT_CRITICAL_ERROR = (
        "Ошибка в программе. функция f.init_PyQt6() вернула недопустимый код возврата -"
    )
    QSS_TEXT = "color: mediumblue;"
    MIN_WIDTH_BUTTON = 150
    KEY_SCROLL_LOCK = Key.scroll_lock
    DELAY_TIME_SECONDS = 0.5
    PATH_DIALOGUE_UI = r"_internal\dialogue.ui"
