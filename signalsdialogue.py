"""Класс и объект сигналов запуска и останова Dialogue"""

from PyQt6.QtCore import QObject, pyqtSignal


class SignalsDialogue(QObject):
    """Класс сигналов запуска и останова Dialogue"""

    start_dialogue = pyqtSignal()
    stop_dialogue = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.parameter_for_signal = -1


# Объект сигналов запуска и останова Dialogue
signals_dialogue = SignalsDialogue()
