"""Модуль с функциями, не привязанными к классам"""

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from pyautogui import hotkey
from time import sleep

from dialogue import Dialogue
from const import Const as C


def press_ctrl(s: str) -> None:
    """
    Эмулировать нажатие клавиш Ctrl+символ.
    :param s: (str). Символ, нажимаемый вместе с Ctrl
    :return: None
    """
    hotkey("ctrl", s)
    sleep(C.DELAY_TIME_SECONDS)


def init_PyQt6():
    """Запускает окно диалога с пользователем"""

    # Получаем существующий экземпляр приложения
    app = QApplication.instance()

    # Если приложения нет, создаем новое
    if not app:
        app = QApplication([])

    # Создаем экземпляр главного окна диалога
    window = Dialogue()
    # Поднимаем окно над остальными окнами
    window.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
    window.show()
    # Делаем окно доступным для ввода с клавиатуры
    window.activateWindow()
    # Запускаем приложение и передаем управление системе
    if not QApplication.instance().startingUp():
        return app.exec()
