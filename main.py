"""Главны модуль программы"""

from sys import exit
import threading

from lsten import Listen
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSharedMemory

from dialogue import Dialogue, SignalsDialogue
import name
import functions as f


def create_signals_dialogue()-> SignalsDialogue:
    """ Создаём объект сигналов и связываем сигналы с функциями обработки """

    # Создаём объект сигналов
    _signals_dialogue = SignalsDialogue()

    # Привязываем сигналы обработки
    _signals_dialogue.start_dialogue.connect(f.window_show)
    _signals_dialogue.end_dialogue.connect(f.window_hide)

    return _signals_dialogue


def start_keyboard_listening()-> None:
    """ Запускаем прослушивание клавиатуры """
    listen = Listen(signals_dialogue)
    listener_thread = threading.Thread(target=listen.listen, daemon=True)
    listener_thread.start()

if __name__ == "__main__":
    # Обеспечиваем загрузку не более одного экземпляра приложения.
    shared_memory = QSharedMemory("UIP")
    if shared_memory.attach():
        exit(1)
    shared_memory.create(1)

    signals_dialogue = create_signals_dialogue()

    # Создаем главное окно диалога. Окно не высвечиваем.
    app = QApplication([])
    name.window = Dialogue(signals_dialogue)

    # Запускаем прослушивание клавиатуры
    start_keyboard_listening()

    # Запускаем приложение
    exit(app.exec())
