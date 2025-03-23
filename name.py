"""Модуль с общими имена программы"""

from dialogue import Dialogue

window: Dialogue | None = None  # Окно диалога (PyQt6).
ret_code_dialogue: int | None = None  # Код возврата из окна диалога
