from dataclasses import dataclass

from pynput.keyboard import Key
from PyQt6.QtGui import QColor


@dataclass(frozen=True, slots=False)
class Const:
    COLOR_MESSAGE_RESTART_PROGRAM = QColor("red")
    COLOR_MESSAGE_START_PROGRAM = QColor("green")
    CTRL = "ctrl"
    EMPTY_TEXT = "f8cd7c4c-0334-4441-af88-8287e77c82e1"
    HASATTR_FROZEN = "frozen"
    KEY_BEGIN_DIALOGUE = Key.scroll_lock  # Клавиша вызова окна диалога
    MAX_CLIPBOARD_READS = 4  # максимально число считываний буфера обмена
    MIN_WIDTH_BUTTON = 170  # Минимальная ширина первых двух кнопок
    PATH_DIALOGUE_UI = (
        r"_internal\dialogue.ui"  # Путь к файлу, сформированному Qt Designer
    )
    QSS_BUTTON = "font-weight: bold; font-size: 12pt; "
    QSS_NO = "color: darkblue;"
    QSS_TEXT = "color: mediumblue;"  # Силь текстовых полей диалога
    QSS_YES = "color: blue;"
    QT_ENVIRON_KEY = "QT_LOGGING_RULES"
    QT_ENVIRON_VALUE = "qt.qpa.window=false"
    TEXT_CANCEL_BUTTON = "Выгрузить программу\nНажми 3"
    TEXT_CRITICAL_ERROR_1 = (
        "Ошибка в программе. Функция window_hide. Неизвестная команда от Dialogue -"
    )
    LOGGER_FILE_NAME = "keyboard.log"
    LOGGER_FORMAT = "%(asctime)s %(levelname)s %(message)s"
    LOGGER_TEXT_BEEN_READ = "В буфер обмена считан выделенный текст"
    LOGGER_TEXT_ERROR_READ = "Выделенный текст не удалось скопировать в буфер обмена"
    LOGGER_TEXT_LOAD_PROGRAM = "Программа загружена"
    LOGGER_TEXT_NO_BEEN_READ = (
        "Неудачная попытка чтения выделенного текста. Время задержки ="
    )
    LOGGER_TEXT_PRESS_CTRL = "Нажали ctrl"
    LOGGER_TEXT_RESTART_PROGRAM = "Повторный вызов программы"
    LOGGER_TEXT_UNLOAD_PROGRAM = "Программа выгружена"
    LOGGER_TEXT_WRITE = "Из буфера обмена отправлен текст"
    TEXT_MESSAGE_RESTART_PROGRAM = "Программа замены регистра текста уже запущена"
    TEXT_MESSAGE_START_PROGRAM = (
        "Запущена программа замены регистра выделенного текста. Горячая клавиша"
    )
    TEXT_NO_BUTTON = "Не заменять\nНажми 2/Esc"
    TEXT_YES_BUTTON = "Заменить\nНажми 1"
    TIME_DELAY_CTRL_C = 0.1  # Задержка, в секундах, после нажатия Ctrl+c
    TIME_DELAY_CTRL_V = 0.4  # Задержка, в секундах, после нажатия Ctrl+v
    TIME_MESSAGE_RESTART_PROGRAM = (
        2  # Время, в секундах, высвечивания сообщения о повторном запуске программы
    )
    TIME_MESSAGE_START_PROGRAM = (
        0.3  # Время высвечивания сообщения о запуске программы (в секундах)
    )
    UUID_PROGRAM = "8A63F9A8-A206-4B0A-B517-F28E3471154E"
