from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QKeyEvent
import functions as f


class CustomTextEdit(QTextEdit):
    """Расширение класса QTextEdit для обработки нажатия специальных клавиш"""

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Переопределение метода. Перехватываем ввод с клавиатуры.
        Обрабатываем специальные клавиши
        :param event: (QKeyEvent). Событие нажатия клавиши
        :return: None
        """
        if not f.run_special_key(event):  # Обрабатываем специальные клавиши
            super().keyPressEvent(
                event
            )  # Для остальных клавиш передаём обработку системе
