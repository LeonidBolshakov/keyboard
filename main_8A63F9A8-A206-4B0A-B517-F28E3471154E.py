"""Главный модуль программы"""

from sys import exit
import threading
import os
import logging

import keyboard
import hotkeys
from PyQt6.QtWidgets import QApplication, QMessageBox

from dialogue import Dialogue
from const import Const as C
import signals
import functions as f


def is_admin():
    try:
        os.listdir(r"C:\Windows\Temp")  # Любое действие, требующее прав
        return True
    except PermissionError:
        return False


def setup_margins(_window: Dialogue) -> None:
    _window.setContentsMargins(*C.MARGIN_MAIN_WINDOW)


def setup_connections(_window: Dialogue) -> None:
    """Связываем сигнал с функцией обработки"""

    _signals = signals.signals
    _signals.start_dialogue.connect(_window.start_dialogue)
    _signals.on_Yes.connect(_window.on_Yes)
    _signals.on_No.connect(_window.on_No)
    _signals.on_Cancel.connect(_window.on_Cancel)


def listen():
    """Прослушивание клавиатуры"""
    hotkeys.set_hotkeys()  # Установка горячих клавиш
    keyboard.wait()


def start_keyboard_listening() -> None:
    """Запускаем прослушивание клавиатуры9"""
    listener_thread = threading.Thread(target=listen, daemon=True)
    listener_thread.start()


def main():
    # Запускаем логирование
    logging.basicConfig(
        level=logging.INFO, filename=C.LOGGER_FILE_PATH, format=C.LOGGER_FORMAT
    )

    f.set_layout_id(
        C.LAYOUT_EN_US
    )  # Устанавливаем английскую раскладку клавиатуры. Это необходимо для правильной работы Ctrl+C -> Ctrl+V
    os.environ[C.QT_ENVIRON_KEY] = C.QT_ENVIRON_VALUE  # Блокируем вывод сообщений о GPA

    # Запускаем прослушивание клавиатуры
    start_keyboard_listening()
    # Создаем приложение.
    app = QApplication([])

    # Проверка запуска программы от имени администратора
    if not is_admin():
        QMessageBox.warning(
            None, C.TITLE_WARNING, C.TEXT_NO_ADMIN, QMessageBox.StandardButton.Ok
        )

    # Сообщаем головной программе, что можно изменять регистр клавиатуры
    print(f"{C.CHECK_COMPLETED}", flush=True)

    # Создаём главное окно диалога. Окно не высвечиваем.
    window = Dialogue()
    setup_margins(window)  # Установка границ окна
    setup_connections(window)

    # Запускаем приложение
    exit(app.exec())


if __name__ == "__main__":
    main()
