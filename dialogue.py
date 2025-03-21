"""Классы сигналов и организации диалога с пользователем"""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtWidgets import (
    QTextBrowser,
    QMainWindow,
    QApplication,
    QDialogButtonBox,
    QPushButton,
)

from replacetext import ReplaceText
from const import Const as C
import name


class KeyPressHandler(QObject):
    """Класс сигналов"""

    keyPressed = pyqtSignal()
    endProcess = pyqtSignal()


# noinspection PyUnresolvedReferences
class Dialogue(QMainWindow):
    """Класс организации диалога с пользователем"""

    # Переменные класса, определённые в Qt Designer
    txtBrowSource: QTextBrowser
    txtBrowReplace: QTextBrowser
    buttonBox: QDialogButtonBox
    yes_button: QPushButton
    no_button: QPushButton
    cancel_button: QPushButton

    def __init__(self, key_handler: KeyPressHandler):
        super().__init__()
        self.key_handler = key_handler
        self.clipboard_text = ""

        self.init_UI()  # Загружаем файл, сформированный Qt Designer
        self.init_var()  # Инициализируем переменные
        self.connect()  # Назначаем обработчики для событий
        self.custom_UI()  # Делаем пользовательские настройки интерфейса

    def keyPressEvent(self, event):
        """Перехватываем ввод с клавиатуры"""
        match event.key():
            case Qt.Key.Key_1:  # Заменять текст
                self.on_Yes()
            case Qt.Key.Key_Escape:  # Отказ от замены
                self.on_No()
            case Qt.Key.Key_2:  # Отказ от замены
                self.on_No()
            case Qt.Key.Key_3:  # Выгрузить программу
                self.on_Cancel()
            case _:
                # Для остальных клавиш передаём обработку системе
                super().keyPressEvent(event)

    def closeEvent(self, event):
        """Перехватываем закрытие окна Пользователем"""
        name.ret_code_dialogue = 0
        self.key_handler.endProcess.emit()
        event.ignore()

    def init_UI(self) -> None:
        """Загрузка UI и атрибутов полей в объект класса"""
        exe_directory = (  # Директория, из которой была запущена программа
            Path(sys.argv[0]).parent
            if hasattr(sys, "frozen")  # exe файл, получен с помощью PyInstaller
            else Path(__file__).parent  # Если файл запущен как обычный Python-скрипт
        )

        ui_config_abs_path = exe_directory / C.PATH_DIALOGUE_UI
        uic.loadUi(ui_config_abs_path, self)

    def init_var(self):
        """Присваиваем значения переменным программы"""
        self.yes_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Yes)
        self.no_button = self.buttonBox.button(QDialogButtonBox.StandardButton.No)
        self.cancel_button = self.buttonBox.button(
            QDialogButtonBox.StandardButton.Cancel
        )

    def connect(self):
        """Назначаем обработчики событий для клика кнопок"""
        self.yes_button.clicked.connect(self.on_Yes)
        self.no_button.clicked.connect(self.on_No)
        self.cancel_button.clicked.connect(self.on_Cancel)

    def custom_UI(self):
        """Пользовательская настройка интерфейса"""
        # Устанавливаем названия и стили кнопок
        self.yes_button.setMinimumWidth(C.MIN_WIDTH_BUTTON)
        self.yes_button.setStyleSheet(C.QSS_REPLACEMENT + C.QSS_BUTTON)
        self.yes_button.setText(C.TEXT_YES_BUTTON)
        self.no_button.setMinimumWidth(C.MIN_WIDTH_BUTTON)
        self.no_button.setStyleSheet(C.QSS_NO_REPLACEMENT + C.QSS_BUTTON)
        self.no_button.setText(C.TEXT_NO_BUTTON)
        self.cancel_button.setText(C.TEXT_CANCEL_BUTTON)
        self.txtBrowReplace.setStyleSheet(C.QSS_TEXT)
        self.txtBrowSource.setStyleSheet(C.QSS_TEXT)

        # Устанавливаем фокус на первую кнопку
        self.yes_button.setFocus()
        # Определяем, что если на кнопке установлен фокус, то при нажатии Enter она считается нажатой.
        self.yes_button.setAutoDefault(True)
        self.no_button.setAutoDefault(True)
        self.cancel_button.setAutoDefault(True)

    def remember_clipboard(self):
        """Запоминаем буфер обмена"""
        self.clipboard_text = QApplication.clipboard().text()

    def display_clipboard(self):
        """Визуализируем буфер обмена"""
        self.txtBrowSource.setText(self.clipboard_text)

    def display_replacements(self):
        """Рассчитываем и отображаем вариант замены текста."""

        replace_text = ReplaceText()
        self.txtBrowReplace.setText(
            replace_text.swap_keyboard_layout(self.clipboard_text)
        )

    @staticmethod
    def text_to_clipboard(text: str) -> None:
        """Записываем текст в буфер обмена"""
        clipboard = QApplication.clipboard()
        if clipboard:
            clipboard.setText(text)

    def on_Yes(self):
        """Записываем вариант замены текста в буфер обмена"""
        # name.ret_code_dialogue == 1 - указание головной программе вставить текст из буфера обмена
        self.text_to_clipboard(self.txtBrowReplace.toPlainText())
        name.window.hide()
        name.ret_code_dialogue = 1
        self.key_handler.endProcess.emit()

    def on_No(self):
        """Отказ от замены текста"""
        # name.ret_code_dialogue == 2 - указание головной программе не заменять текст
        name.ret_code_dialogue = 2
        self.key_handler.endProcess.emit()

    @staticmethod
    def on_Cancel():
        """Выгружаем программу"""
        QApplication.quit()

    def processing_clipboard(self):
        self.remember_clipboard()  # запоминаем буфера обмена
        self.display_clipboard()  # Визуализируем буфера обмена
        self.display_replacements()  # Рассчитываем и отображаем вариант замены теста
