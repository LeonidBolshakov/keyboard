"""Класс для прослушивания клавиатуры"""

import logging

logger = logging.getLogger(__name__)

from pynput.keyboard import Key, KeyCode, Listener

from const import Const as C
import signals


class Listen:
    """Класс для прослушивания клавиатуры с целью стартовать диалог"""

    def __init__(self):
        self.signals = signals.signals  # Сигналы старт/стоп Dialogue

    def on_release(self, key: Key | KeyCode) -> None:
        """
        Обработка отпуская клавиши
        :param key: (Key | KeyCode) - отпущенная клавиша
        :return: None
        """
        if signals.signals.debug:
            logger.info(f'   ->{key}')
        if key == C.KEY_BEGIN_DIALOGUE:  # Клавиша вызова окна диалога
            # Генерация сигнала "Начало диалога"
            self.signals.start_dialogue.emit()

    def listen(self):
        """Прослушивание клавиатуры"""
        with Listener(on_press=None, on_release=self.on_release) as listener:
            listener.join()
