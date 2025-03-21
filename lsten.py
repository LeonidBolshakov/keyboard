"""Класс для прослушивания клавиатуры"""

from pynput.keyboard import Key, KeyCode, Listener

import functions as f
from const import Const as C
from dialogue import KeyPressHandler


class Listen:
    """Класс для прослушивания клавиатуры"""

    def __init__(self, key_handler: KeyPressHandler):
        self.key_handler = key_handler  # Сигнал отпускания клавиши вызова диалога

    def on_release(self, key: Key | KeyCode) -> None:
        """
        Обработка отпуская клавиши
        :param key: (Key | KeyCode) - отпущенная клавиша
        :return: None
        """
        if key == C.KEY_SCROLL_LOCK:  # Клавиша вызова окна диалога
            # Эмуляция Ctrl+c
            f.press_ctrl("c")
            # Генерация сигнала "Нажатие клавиши вызова"
            self.key_handler.keyPressed.emit()

    def listen(self):
        """Прослушивание клавиатуры"""
        with Listener(on_press=None, on_release=self.on_release) as listener:
            listener.join()
