from PyQt6.QtWidgets import QTextBrowser
from PyQt6.QtGui import QKeyEvent
import functions as f


class CustomTextBrowser(QTextBrowser):
    """Расширение класса QTextBrowser для обработки нажатия специальных клавиш"""

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Переопределение метода. Перехватываем ввод с клавиатуры.
        Обрабатываем специальные клавиши
        :param event: (QKeyEvent). Событие нажатия клавиши
        :return: None
        """
        if not f.special_key(event):  # Обрабатываем специальные клавиши
            super().keyPressEvent(
                event
            )  # Для остальных клавиш передаём обработку системе
