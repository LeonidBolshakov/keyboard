"""Главны модуль программы"""

import ctypes
from sys import exit
import threading
import os

from lsten import Listen
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSharedMemory

from dialogue import Dialogue, KeyPressHandler
import name
import functions as f

if __name__ == "__main__":
    shared_memory = QSharedMemory("UIP")
    if shared_memory.attach():
        exit(1)
    if not shared_memory.create(1):
        raise ValueError
    # Подавляем предупреждения qt.qpa.window
    os.environ["QT_LOGGING_RULES"] = "qt.qpa.window=false"

    # Создаём объект сигналов
    key_handler = KeyPressHandler()
    key_handler.keyPressed.connect(f.window_show)
    key_handler.endProcess.connect(f.window_hide)

    # Создаем главное окно диалога. Окно не высвечиваем.
    app = QApplication([])
    name.window = Dialogue(key_handler)

    # Запускаем прослушивание клавиатуры
    listen = Listen(key_handler)
    listener_thread = threading.Thread(target=listen.listen, daemon=True)
    listener_thread.start()

    # Запускаем приложение
    exit(app.exec())
