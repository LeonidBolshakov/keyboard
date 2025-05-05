"""Класс и объект сигнала запуска Dialogue"""

from PyQt6.QtCore import QObject, pyqtSignal


class Signals(QObject):
    """Класс сигнала запуска Dialogue"""

    start_dialogue = pyqtSignal()
    on_Yes = pyqtSignal()
    on_No = pyqtSignal()
    on_Cancel = pyqtSignal()
    debug = False
    current_layout = 0


# Объект сигналов запуска и останова Dialogue
signals = Signals()
