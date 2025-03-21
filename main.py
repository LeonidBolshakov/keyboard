"""Главны модуль программы"""

import ctypes
from sys import exit
import threading
import os

from lsten import Listen
from PyQt6.QtWidgets import QApplication

from dialogue import Dialogue, KeyPressHandler
import name
import functions as f

if __name__ == "__main__":
    # Создаём объект сигналов
    key_handler = KeyPressHandler()
    key_handler.keyPressed.connect(f.window_show)
    key_handler.endProcess.connect(f.window_hide)


    # Подавляем предупреждения qt.qpa.window
    os.environ["QT_LOGGING_RULES"] = "qt.qpa.window=false"
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Обработка больших DPI

    # Создаем главное окно диалога. Окно не высвечиваем.
    app = QApplication([])
    name.window = Dialogue(key_handler)

    # Запускаем прослушивание клавиатуры
    listen = Listen(key_handler)
    listener_thread = threading.Thread(target=listen.listen, daemon=True)
    listener_thread.start()

    # Запускаем приложение
    exit(app.exec())
