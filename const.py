from dataclasses import dataclass

from pynput.keyboard import Key
from PyQt6.QtGui import QColor


@dataclass(frozen=True, slots=False)
class Const:
    COLOR_MESSAGE_RESTART_PROGRAM = QColor("red")
    COLOR_MESSAGE_START_PROGRAM = QColor("green")
    KEY_BEGIN_DIALOGUE = Key.scroll_lock  # Клавиша вызова окна диалога
    MIN_WIDTH_BUTTON = 150  # Минимальная ширина первых двух кнопок
    PATH_DIALOGUE_UI = (
        r"_internal\dialogue.ui"  # Путь к файлу, сформированному Qt Designer
    )
    QSS_BUTTON = "font-weight: bold; font-size: 12pt; "
    QSS_NO = "color: darkblue;"
    QSS_TEXT = "color: mediumblue;"  # Силь текстовых полей диалога
    QSS_YES = "color: blue;"
    TEXT_CANCEL_BUTTON = "Выгрузить программу\nНажми 3"
    TEXT_CRITICAL_ERROR_1 = (
        "Ошибка в программе. Функция window_hide. Неизвестная команда от Dialogue -"
    )
    TEXT_CRITICAL_ERROR_2 = "Ошибка в программе. Функция f.window_show. Переменная name.window не инициализирована"
    TEXT_MESSAGE_RESTART_PROGRAM = "Программа замены регистра текста уже запущена"
    TEXT_MESSAGE_START_PROGRAM = (
        "Запущена программа замены регистра выделенного текста. Горячая клавиша"
    )
    TEXT_NO_BUTTON = "Не заменять\nНажми 2/Esc"
    TEXT_YES_BUTTON = "Заменить\nНажми 1"
    TIME_DELAY_CTRL = 0.2  # Задержка, в секундах, после нажатия Ctrl+Клавиша
    TIME_MESSAGE_RESTART_PROGRAM = (
        2  # Время, в секундах, высвечивания сообщения о повторном запуске программы
    )
    TIME_MESSAGE_START_PROGRAM = (
        0.3  # Время высвечивания сообщения о запуске программы (в секундах)
    )
    UUID_PROGRAM = "8A63F9A8-A206-4B0A-B517-F28E3471154E"
