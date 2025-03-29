"""Классы сигналов и организации диалога с пользователем"""

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
import signalsdialogue
import functions as f


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

    def __init__(self, restart_program: bool) -> None:
        """
        Создание объекта класса
        :param restart_program: (bool) - признак повторного запуска программы
        """
        super().__init__()

        # При повторном запуске программы процесс прекращается.
        if restart_program:
            f.show_message(
                C.TEXT_MESSAGE_RESTART_PROGRAM,
                C.TIME_MESSAGE_RESTART_PROGRAM,
                C.COLOR_MESSAGE_RESTART_PROGRAM,
            )
            sys.exit(1)

        # Информирование пользователя о загрузке программы
        f.show_message(
            f"{C.TEXT_MESSAGE_START_PROGRAM} {C.KEY_BEGIN_DIALOGUE}",
            C.TIME_MESSAGE_START_PROGRAM,
            C.COLOR_MESSAGE_START_PROGRAM,
        )

        self.signals_dialogue = signalsdialogue.signals_dialogue
        self.clipboard_text = ""

        self.init_UI()  # Загружаем файл, сформированный Qt Designer
        self.init_var()  # Инициализируем переменные
        self.connect()  # Назначаем обработчики событий
        self.custom_UI()  # Делаем пользовательские настройки интерфейса

    def keyPressEvent(self, event):
        """Переопределение метода. Перехватываем ввод с клавиатуры"""
        match event.key():
            case Qt.Key.Key_1:  # Заменять текст
                self.on_Yes()
            case Qt.Key.Key_Escape:  # Отказ от замены
                self.on_No()
            case Qt.Key.Key_2:  # Отказ от замены
                self.on_No()
            case Qt.Key.Key_3:  # Выгрузить программу
                f.on_Cancel()
            case _:
                # Для остальных клавиш передаём обработку системе
                super().keyPressEvent(event)

    def closeEvent(self, event):
        """Переопределение метода. Перехватываем закрытие окна Пользователем"""
        # При закрытии окна пользователем сигнализируем об остановке диалога, но программу из памяти не выгружаем
        self.signals_dialogue.parameter_for_signal = 0
        self.signals_dialogue.stop_dialogue.emit()
        event.ignore()

    def init_UI(self) -> None:
        """Загрузка UI и атрибутов полей в объект класса"""
        exe_directory = (  # Директория, из которой была запущена программа
            Path(sys.argv[0]).parent
            if hasattr(sys, "frozen")  # exe файл, получен с помощью PyInstaller
            else Path(__file__).parent  # Файл запущен как обычный Python-скрипт
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
        self.cancel_button.clicked.connect(f.on_Cancel)

    def custom_UI(self):
        """Пользовательская настройка интерфейса"""

        # Устанавливаем размеры, стили, свойства и названия кнопок
        f.making_button_settings(self.yes_button, C.TEXT_YES_BUTTON, C.QSS_YES)
        f.making_button_settings(self.no_button, C.TEXT_NO_BUTTON, C.QSS_NO)
        f.making_button_settings(self.cancel_button, C.TEXT_CANCEL_BUTTON)

        # Устанавливаем стили текстовых полей
        self.txtBrowReplace.setStyleSheet(C.QSS_TEXT)
        self.txtBrowSource.setStyleSheet(C.QSS_TEXT)

        # Устанавливаем фокус на первую кнопку
        self.yes_button.setFocus()

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

    def on_Yes(self):
        """Заменяем выделенный текст предложенным вариантом замены"""
        f.text_to_clipboard(self.txtBrowReplace.toPlainText())
        self.hide()  # Освобождаем фокус для окна с выделенным текстом
        self.signals_dialogue.parameter_for_signal = (
            1  # указание головной программе вставить текст из буфера обмена
        )
        self.signals_dialogue.stop_dialogue.emit()

    def on_No(self):
        """Отказ от замены текста"""
        self.signals_dialogue.parameter_for_signal = (
            2  # указание головной программе не заменять текст
        )
        self.signals_dialogue.stop_dialogue.emit()

    def processing_clipboard(self):
        self.remember_clipboard()  # запоминаем буфера обмена
        self.display_clipboard()  # Визуализируем буфера обмена
        self.display_replacements()  # Рассчитываем и отображаем вариант замены теста

    def window_show(self) -> None:
        """
        Показ окна диалога.
        :return: None
        """
        # Поднимаем окно над всеми окнами
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.processing_clipboard()  # Обрабатываем буфер обмена
        self.show()  # Выводим окно на экран
        # Делаем окно доступным для ввода с клавиатуры
        self.activateWindow()

    def window_hide(self) -> None:
        """выполняем команду, заданную в параметре сигнала и останавливаем работу с диалогом"""

        rc = self.signals_dialogue.parameter_for_signal
        # Обрабатываем ко
        match rc:
            case 0:  # Выгрузка программы
                pass
            case 1:  # Заменяем выделенный текст
                f.press_ctrl("v", C.TIME_DELAY_CTRL_V)  # Эмуляция Ctrl+v
            case 2:  # Отказ от замены текста
                pass
            case _:  # Непредусмотренная команда
                logger.critical(
                    f"{C.TEXT_CRITICAL_ERROR_1} {self.signals_dialogue.parameter_for_signal =}"
                )

        self.hide()  # Убираем окно с экрана
