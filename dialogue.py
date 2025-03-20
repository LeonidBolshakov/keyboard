"""Класс организации диалога с пользователем"""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QTextBrowser,
    QMainWindow,
    QApplication,
    QDialogButtonBox,
    QPushButton,
)

from replacetext import ReplaceText
from const import Const as C


class Dialogue(QMainWindow):
    # Переменные класса, определённые в Qt Designer
    txtBrowSource: QTextBrowser
    txtBrowReplace: QTextBrowser
    buttonBox: QDialogButtonBox
    yes_button: QPushButton
    no_button: QPushButton
    cancel_button: QPushButton

    def __init__(self):
        super().__init__()
        self.clipboard_text = ""

        self.init_UI()  # Загружаем файл, сформированный Qt Designer
        self.init_var()  # Инициализируем переменные
        self.connect()  # Назначаем обработчики для событий
        self.custom_UI()  # Делаем пользовательские настройки интерфейса
        self.remember_clipboard()  # запоминаем буфера обмена
        self.display_clipboard()  # Визуализация буфера обмена
        self.display_replacements()  # Рассчитываем и отображаем варианты замены теста

    def keyPressEvent(self, event):
        """Перехватываем ввод с клавиатуры"""
        match event.key():
            case Qt.Key.Key_1:  # Заменять текст
                self.on_Yes()
            case Qt.Key.Key_Escape:  # Выгрузить программу
                self.on_No()
            case Qt.Key.Key_2:  # Выгрузить программу
                self.on_No()
            case Qt.Key.Key_3:  # Отказ от замены
                self.on_Cancel()
            case _:
                super().keyPressEvent(event)

    def init_UI(self) -> None:
        """Загрузка UI и атрибутов полей в объект класса"""

        exe_directory = (  # Директория, из которой была запущена программа
            Path(sys.argv[0]).parent
            if hasattr(sys, "frozen")  # exe файл, получен с помощью PyInstaller
            else Path(__file__).parent  # Если файл запущен как обычный Python-скрипт
        )

        ui_config_abs_path = exe_directory / "dialogue.ui"
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
        self.yes_button.setText(C.TEXT_YES_BUTTON)
        self.yes_button.setStyleSheet(C.QSS_REPLACEMENT + C.QSS_BUTTON)
        self.txtBrowReplace.setStyleSheet(C.QSS_REPLACEMENT)
        self.no_button.setText(C.TEXT_NO_BUTTON)
        self.no_button.setStyleSheet(C.QSS_NO_REPLACEMENT + C.QSS_BUTTON)
        self.txtBrowSource.setStyleSheet(C.QSS_NO_REPLACEMENT)
        self.cancel_button.setText(C.TEXT_CANCEL_BUTTON)

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
        # Выход из программы с кодом, отличным от 1 - указание головной программе вставить текст из буфера обмена
        self.text_to_clipboard(self.txtBrowReplace.toPlainText())
        QApplication.exit(1)

    @staticmethod
    def on_No():
        """Отказ от замены текста"""
        # Выход из программы с кодом, отличным от 2 - указание головной программе не заменять текст
        QApplication.exit(2)

    @staticmethod
    def on_Cancel():
        """Прекращаем диалог"""
        # Выход из программы с кодом 3 - указание головной программе выгрузить программу
        QApplication.exit(3)
