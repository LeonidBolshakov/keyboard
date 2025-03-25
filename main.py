"""Главный модуль программы"""

from sys import exit
from os import environ
import threading

from lsten import Listen
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSharedMemory

from dialogue import Dialogue, SignalsDialogue
import name
import functions as f
from const import Const as C


def create_signals_dialogue() -> SignalsDialogue:
    """Создаём сигналы и связываем их с функциями обработки"""

    # Создаём объект сигналов
    _signals_dialogue = SignalsDialogue()

    # Привязываем сигналы обработки
    _signals_dialogue.start_dialogue.connect(f.window_show)
    _signals_dialogue.stop_dialogue.connect(f.window_hide)

    return _signals_dialogue


def start_keyboard_listening() -> None:
    """Запускаем прослушивание клавиатуры"""
    listen = Listen(signals_dialogue)
    listener_thread = threading.Thread(target=listen.listen, daemon=True)
    listener_thread.start()


if __name__ == "__main__":
    # Блокируем вывод сообщений о GPA
    environ["QT_LOGGING_RULES"] = "qt.qpa.window=false"

    # Проверка повторного запуска.
    shared_memory = QSharedMemory(C.UUID_PROGRAM)
    shared_memory.attach()
    if shared_memory.data():
        is_restart_program = True
    else:
        shared_memory.create(1)
        is_restart_program = False

    # Создаём сигналы старта и остановки работы класса dialogue
    signals_dialogue = create_signals_dialogue()

    # Создаем главное окно диалога. Окно не высвечиваем.
    app = QApplication([])
    name.window = Dialogue(signals_dialogue, is_restart_program)

    # Запускаем прослушивание клавиатуры
    start_keyboard_listening()

    # Запускаем приложение
    exit(app.exec())
