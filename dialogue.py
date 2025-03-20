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
    txtBrowReplace1: QTextBrowser
    txtBrowReplace2: QTextBrowser
    buttonBox: QDialogButtonBox
    yes_button: QPushButton
    ok_button: QPushButton
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
            case Qt.Key.Key_1:  # Выбран первый вариант замены
                self.on_Yes()
            case Qt.Key.Key_2:  # Выбран второй вариант замены
                self.on_Ok()
            case Qt.Key.Key_Escape:  # Отказ от замены
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
        self.ok_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        self.cancel_button = self.buttonBox.button(
            QDialogButtonBox.StandardButton.Cancel
        )

    def connect(self):
        """Назначаем обработчики событий для клика кнопок"""
        self.yes_button.clicked.connect(self.on_Yes)
        self.ok_button.clicked.connect(self.on_Ok)
        self.cancel_button.clicked.connect(self.on_Cancel)

    def custom_UI(self):
        """Пользовательская настройка интерфейса"""
        # Устанавливаем названия кнопок
        self.yes_button.setText(C.TEXT_YES_BUTTON)
        self.ok_button.setText(C.TEXT_OK_BUTTON)
        self.cancel_button.setText(C.TEXT_CANCEL_BUTTON)

        # Устанавливаем фокус на первую кнопку
        self.yes_button.setFocus()
        # Определяем, что если на кнопке установлен фокус, то при нажатии Enter она считается нажатой.
        self.yes_button.setAutoDefault(True)
        self.ok_button.setAutoDefault(True)
        self.cancel_button.setAutoDefault(True)

    def remember_clipboard(self):
        """Запоминаем буфер обмена"""
        self.clipboard_text = QApplication.clipboard().text()

    def display_clipboard(self):
        """Визуализируем буфер обмена"""
        self.txtBrowSource.setText(self.clipboard_text)

    def display_replacements(self):
        """
        Рассчитываем и отображаем варианты замены текста.
        С английского регистра на русский и с русского на английский
        """
        replace_text = ReplaceText()
        # self.txtBrowReplace1.setText(replace_text.translate_text(self.clipboard_text))
        self.txtBrowReplace1.setText(
            replace_text.swap_keyboard_layout(self.clipboard_text)
        )
        reverse_translate_text = replace_text.reverse_translate_text(
            self.clipboard_text
        )
        self.txtBrowReplace2.setText(reverse_translate_text)

    @staticmethod
    def text_to_clipboard(text: str) -> None:
        """Записываем текст в буфер обмена"""
        clipboard = QApplication.clipboard()
        if clipboard:
            clipboard.setText(text)

    def on_Yes(self):
        """Записываем первый вариант замены текста в буфер обмена"""
        # Выход из программы с кодом, отличным от 0 - указание головной программе вставить текст из буфера обмена
        self.text_to_clipboard(self.txtBrowReplace1.toPlainText())
        QApplication.exit(1)

    def on_Ok(self):
        """Записываем второй вариант замены текста в буфер обмена"""
        # Выход из программы с кодом, отличным от 0 - указание головной программе вставить текст из буфера обмена
        self.text_to_clipboard(self.txtBrowReplace2.toPlainText())
        QApplication.exit(2)

    @staticmethod
    def on_Cancel():
        """Прекращаем диалог"""
        # Выход из программы с кодом 0 - указание головной программе НЕ вставлять текст из буфера обмена
        QApplication.exit(0)
