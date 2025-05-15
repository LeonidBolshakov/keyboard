from dataclasses import dataclass

from PyQt6.QtGui import QColor


@dataclass(frozen=True, slots=False)
class Const:
    COLOR_MESSAGE_RESTART_PROGRAM = QColor("red")
    COLOR_MESSAGE_START_PROGRAM = QColor("green")
    CTRL = "ctrl"  # Ctrl+c, Ctrl+v
    HASATTR_FROZEN = "frozen"
    HOTKEY_BEGIN_DIALOGUE = "scroll lock"  # Клавиша вызова окна замены регистров
    HOTKEY_CHANGE_REGISTER = "caps lock"
    HOTKEY_MAIL = "3"
    HOTKEY_MODIFIER = "ctrl+shift"  # Модификатор горячих цифровых клавиш
    HOTKEY_MY_SIGNATURE = "9"
    HOTKEY_TEL = "4"
    KEY_CHANGE_REGISTER = "alt+right shift"
    KEY_SIGN2 = "shift+enter"
    LAYOUT_EN_US = 0x409
    LOGGER_FILE_PATH = r"c:\temp\keyboard.log"
    LOGGER_FORMAT = "%(asctime)s %(levelname)s %(message)s"
    LOGGER_TEXT_ERROR_NUM_PARAM = (
        "У программы 1 параметр Код шаблона клавиатуры. Передано параметров."
    )
    LOGGER_TEXT_ERROR_PARAM = (
        "Параметр программы десятичное или шестнадцатеричное число."
        "Например 0x409. Передан параметр"
    )
    LOGGER_TEXT_ERROR_READ = "Выделенный текст не удалось скопировать в буфер обмена"
    LOGGER_TEXT_LOAD_PROGRAM = "Программа загружена"
    LOGGER_TEXT_NO_READ = (
        "Неудачная попытка чтения выделенного текста. Время задержки ="
    )
    LOGGER_TEXT_CHANGE = "Исходный текст -  "
    LOGGER_TEXT_RESTART_PROGRAM = "Повторный вызов программы"
    LOGGER_TEXT_RESTORED_CLIPBOARD = "Восстановили буфер обмена"
    LOGGER_TEXT_START_DIALOGUE = "Старт диалога. Заголовок окна"
    LOGGER_TEXT_STOP_DIALOGUE = "Остановка диалога."
    LOGGER_TEXT_UNLOAD_PROGRAM = "Программа выгружена"
    LOGGER_TEXT_WRITE = "Из буфера обмена отправлен текст"
    MARGIN_MAIN_WINDOW = (20, 20, 20, 20)
    MAX_CLIPBOARD_READS = 2  # максимально число считываний буфера обмена
    MIN_WIDTH_BUTTON = 170  # Минимальная ширина первых двух кнопок
    MODUL_NAME = "main_8A63F9A8-A206-4B0A-B517-F28E3471154E.py"
    PATH_DIALOGUE_UI = (
        r"_internal\dialogue.ui"  # Путь к файлу, сформированному Qt Designer
    )
    PM_HWND_BROADCAST = 0xFFFF  # дескриптор окна (0xFFFF для отправки всем окнам)
    PM_WM_INPUTLANGCHANGEREQUEST = (
        0x50  # Код сообщения. Запрос на смену раскладки клавиатуры
    )
    PM_FLAG_CHANGE = 0  # Запрос на изменение

    PID_FILE_PATH = f"c:\\temp\\{MODUL_NAME}.txt"

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
    TEXT_WRITE_MAIL = "bolleoa@gmail.com"
    TEXT_MESSAGE_RESTART_PROGRAM = "Программа замены регистра текста уже запущена"
    TEXT_MESSAGE_START_PROGRAM = (
        "Запущена программа замены регистра выделенного текста. Горячая клавиша"
    )
    TEXT_NO_ADMIN = (
        "Программа запущена НЕ с правами администратора\nВозможна неустойчивая работа"
    )
    TEXT_NO_ENG_LAYOUT = (
        "Раскладка клавиатуры НЕ английская\nПрограмма будет работать с ограничениями"
    )
    TEXT_NO_BUTTON = "Не заменять\nНажми 2/Esc"
    TEXT_WRITE_TEL = "9025138590"
    TEXT_SIGN1 = "С уважением,"
    TEXT_SIGN3 = "Леонид Большаков"
    TEXT_WINDOW_NOT_FOUND = "-> Окно не найдено <-"
    TEXT_YES_BUTTON = "Заменить\nНажми 1"
    TIME_DELAY_CTRL_C = 0.1  # Задержка, в секундах, после нажатия Ctrl+c
    TIME_DELAY_CTRL_V = 0.1  # Задержка, в секундах, после нажатия Ctrl+v
    TIME_DELAY_SET_LAYOUT = (
        1.5  # Задержка, в секундах, перед установкой раскладки клавиатуры
    )
    TIME_MESSAGE_RESTART_PROGRAM = (
        2  # Время, в секундах, высвечивания сообщения о повторном запуске программы
    )
    TIME_MESSAGE_START_PROGRAM = (
        0.3  # Время высвечивания сообщения о запуске программы (в секундах)
    )
    TITLE_WARNING = "Предупреждение"
