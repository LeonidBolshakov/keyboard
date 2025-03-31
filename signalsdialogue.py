"""Класс и объект сигналов запуска и останова Dialogue"""

from PyQt6.QtCore import QObject, pyqtSignal


class SignalsDialogue(QObject):
    """Класс сигналов запуска и останова Dialogue"""

    start_dialogue = pyqtSignal()


# Объект сигналов запуска и останова Dialogue
signals_dialogue = SignalsDialogue()
