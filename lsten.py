"""Класс для прослушивания клавиатуры"""

from pynput.keyboard import Key, KeyCode, Listener

import functions as f
from const import Const as C
from dialogue import SignalsDialogue


class Listen:
    """Класс для прослушивания клавиатуры"""

    def __init__(self, signals_dialogue: SignalsDialogue):
        self.signals_dialogue = signals_dialogue  # Сигналы старт/стоп Dialogue

    def on_release(self, key: Key | KeyCode) -> None:
        """
        Обработка отпуская клавиши
        :param key: (Key | KeyCode) - отпущенная клавиша
        :return: None
        """
        if key == C.KEY_BEGIN_DIALOGUE:  # Клавиша вызова окна диалога
            # Эмуляция Ctrl+c
            f.press_ctrl("c")
            # Генерация сигнала "Начало диалога"
            self.signals_dialogue.start_dialogue.emit()

    def listen(self):
        """Прослушивание клавиатуры"""
        with Listener(on_press=None, on_release=self.on_release) as listener:
            listener.join()
