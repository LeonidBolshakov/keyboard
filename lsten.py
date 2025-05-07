"""Класс для прослушивания клавиатуры"""

import logging

logger = logging.getLogger(__name__)

import keyboard

from const import Const as C
import signals
import functions as f


class Listen:
    """Класс для прослушивания клавиатуры с целью стартовать диалог"""

    def __init__(self):
        self.signals = signals.signals  # Сигналы старт/стоп Dialogue

    def on_press(self, event: keyboard._keyboard_event.KeyboardEvent) -> None:
        """
        Обработка нажатия клавиши
        :param event - событие
        :return: None
        """
        if event.name == C.KEY_BEGIN_DIALOGUE:  # Клавиша вызова окна диалога
            # Генерация сигнала "Начало диалога"
            self.signals.start_dialogue.emit()

    def listen(self):
        """Прослушивание клавиатуры"""
        keyboard.on_press(self.on_press)
        # f.set_layout(signals.Signals.current_layout)
        # print(f.get_current_layout())
        keyboard.wait()
