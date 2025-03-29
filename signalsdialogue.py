"""Модуль с общими имена программы"""

from PyQt6.QtCore import QObject, pyqtSignal


class SignalsDialogue(QObject):
    """Класс сигналов запуска и останова Dialogue"""

    start_dialogue = pyqtSignal()
    stop_dialogue = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.parameter_for_signal = -1


signals_dialogue = SignalsDialogue()
