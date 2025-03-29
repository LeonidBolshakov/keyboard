"""Главный модуль программы"""

from sys import exit
from os import environ
import threading
import logging

from lsten import Listen
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSharedMemory

from dialogue import Dialogue
from const import Const as C
import signalsdialogue


def setup_connections(_window) -> None:
    """Связываем сигналы с функциями обработки"""

    signals_dialogue = signalsdialogue.signals_dialogue

    signals_dialogue.start_dialogue.connect(_window.window_show)
    signals_dialogue.stop_dialogue.connect(_window.window_hide)


def start_keyboard_listening() -> None:
    """Запускаем прослушивание клавиатуры"""
    listen = Listen()
    listener_thread = threading.Thread(target=listen.listen, daemon=True)
    listener_thread.start()


def init_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename=C.LOGGER_FILE_NAME,
        format=C.LOGGER_FORMAT,
    )


if __name__ == "__main__":
    # Блокируем вывод сообщений о GPA
    environ[C.QT_ENVIRON_KEY] = C.QT_ENVIRON_VALUE

    # Проверка повторного запуска.
    shared_memory = QSharedMemory(C.UUID_PROGRAM)
    shared_memory.attach()
    if shared_memory.data():
        is_restart_program = True
    else:
        shared_memory.create(1)
        init_logging()
        is_restart_program = False

    # Создаем главное окно диалога. Окно не высвечиваем.
    app = QApplication([])
    window = Dialogue(is_restart_program)
    setup_connections(window)

    # Запускаем прослушивание клавиатуры
    start_keyboard_listening()

    # Запускаем приложение
    exit(app.exec())
