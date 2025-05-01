"""Главный модуль программы"""

from sys import exit
import threading
import logging
import os

from lsten import Listen
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QSharedMemory

from dialogue import Dialogue
from const import Const as C
import signals


def is_admin():
    try:
        os.listdir(r"C:\Windows\Temp")  # Любое действие, требующее прав
        return True
    except PermissionError:
        return False


def setup_margins():
    window.setContentsMargins(20, 20, 20, 20)


def setup_connections(_window) -> None:
    """Связываем сигнал с функцией обработки"""

    _signals = signals.signals
    _signals.start_dialogue.connect(_window.start_dialogue)
    _signals.on_Yes.connect(_window.on_Yes)
    _signals.on_No.connect(_window.on_No)
    _signals.on_Cancel.connect(_window.on_Cancel)


def start_keyboard_listening() -> None:
    """Запускаем прослушивание клавиатуры"""
    listen = Listen()
    listener_thread = threading.Thread(target=listen.listen, daemon=True)
    listener_thread.start()


def init_logging():
    """Стартуем систему логирования"""
    logging.basicConfig(
        level=logging.INFO,
        filename=C.LOGGER_FILE_NAME,
        format=C.LOGGER_FORMAT,
    )


if __name__ == "__main__":
    # Блокируем вывод сообщений о GPA
    os.environ[C.QT_ENVIRON_KEY] = C.QT_ENVIRON_VALUE

    # Проверка повторного запуска программы.
    shared_memory = QSharedMemory(C.UUID_PROGRAM)
    shared_memory.attach()
    if shared_memory.data():
        is_restart_program = True
    else:
        shared_memory.create(1)
        init_logging()
        is_restart_program = False
        # Запускаем прослушивание клавиатуры
        start_keyboard_listening()

    # Создаем приложение и главное окно диалога. Окно не высвечиваем.
    app = QApplication([])
    # Проверка запуска программы от имени администратора
    if not is_admin():
        QMessageBox.warning(
            None, C.TITLE_WARNING, C.TEXT_NO_ADMIN, QMessageBox.StandardButton.Ok
        )
    window = Dialogue(is_restart_program)
    setup_margins()  # Установка границ окна
    setup_connections(window)

    # Запускаем приложение
    exit(app.exec())
