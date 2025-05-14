"""Класс организации диалога с пользователем"""

import sys
from pathlib import Path
import logging

logger = logging.getLogger()

from PyQt6 import uic
from PyQt6.QtGui import QKeyEvent, QCloseEvent
from PyQt6.QtCore import Qt, QCoreApplication, QTimer
from PyQt6.QtWidgets import QMainWindow, QDialogButtonBox, QPushButton

from const import Const as C
import functions as f
from customtextedit import CustomTextEdit


# noinspection PyUnresolvedReferences
class Dialogue(QMainWindow):
    """Класс организации диалога с пользователем"""

    # Переменные класса, определённые в Qt Designer
    txtEditSource: CustomTextEdit
    txtEditReplace: CustomTextEdit
    buttonBox: QDialogButtonBox
    yes_button: QPushButton
    no_button: QPushButton
    cancel_button: QPushButton

    def __init__(self) -> None:
        """Инициализация объекта класса"""
        super().__init__()

        # Если прежний диалог не закончен - новый не начинаем
        if not self.isHidden():
            return

        # Информирование о первоначальной загрузке программы
        logging.info(C.LOGGER_TEXT_LOAD_PROGRAM)
        f.show_message(
            f"{C.TEXT_MESSAGE_START_PROGRAM} {C.HOTKEY_BEGIN_DIALOGUE}",
            C.TIME_MESSAGE_START_PROGRAM,
            C.COLOR_MESSAGE_START_PROGRAM,
        )

        # Объявление имён
        self.old_clipboard_text = ""
        self.clipboard_text = ""
        self.is_restore_clipboard = True

        self.init_UI()  # Загружаем файл, сформированный Qt Designer
        self.init_var()  # Инициализируем переменные
        self.set_connect()  # Назначаем обработчики событий
        self.custom_UI()  # Делаем пользовательские настройки интерфейса

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

    def closeEvent(self, event: QCloseEvent) -> None:
        """Переопределение метода. Перехватываем закрытие окна Пользователем"""
        # При закрытии окна пользователем сигнализируем об остановке диалога, но программу из памяти не выгружаем
        self.stop_dialogue(2)
        event.ignore()

    def init_UI(self) -> None:
        """Загрузка UI и атрибутов полей в объект класса"""
        exe_directory = (  # Директория, из которой была запущена программа
            Path(sys.argv[0]).parent
            if hasattr(sys, C.HASATTR_FROZEN)  # exe файл, получен с помощью PyInstaller
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

    def set_connect(self):
        """Назначаем обработчики"""

        # Обработчик событий для клика кнопок
        self.yes_button.clicked.connect(self.on_Yes)
        self.no_button.clicked.connect(self.on_No)
        self.cancel_button.clicked.connect(self.on_Cancel)

        # Обработчик изменения копии оригинального текста
        self.txtEditSource.textChanged.connect(self.change_original_text)

    def custom_UI(self):
        """Пользовательская настройка интерфейса"""

        # Устанавливаем размеры, стили, свойства и названия кнопок
        f.making_button_settings(self.yes_button, C.TEXT_YES_BUTTON, C.QSS_YES)
        f.making_button_settings(self.no_button, C.TEXT_NO_BUTTON, C.QSS_NO)
        f.making_button_settings(self.cancel_button, C.TEXT_CANCEL_BUTTON)

        # Устанавливаем стили текстовых полей
        self.txtEditSource.setStyleSheet(C.QSS_TEXT)
        self.txtEditReplace.setStyleSheet(C.QSS_TEXT)

        # Устанавливаем фокус на первую кнопку
        self.yes_button.setFocus()

    def show_original_text(self, original_text: str) -> None:
        """
        Отображаем текст пользователя
        :param original_text: (str)/ текст пользователя
        :return:
        """
        self.txtEditSource.setText(original_text)

    def show_replacements_text(self, replacement_option_text: str) -> None:
        """Отображаем вариант замены текста."""
        self.txtEditReplace.setText(
            f.ReplaceText().swap_keyboard_register(replacement_option_text)
        )

    def on_Yes(self):
        """Заменяем выделенный текст предложенным вариантом замены"""
        f.put_to_clipboard(self.txtEditReplace.toPlainText())
        self.hide()  # Освобождаем фокус для окна с выделенным текстом
        self.stop_dialogue(1)

    @staticmethod
    def on_Cancel() -> None:
        """Выгружаем программу"""
        logger.info(C.LOGGER_TEXT_UNLOAD_PROGRAM)
        QTimer.singleShot(0, QCoreApplication.exit)

    def on_No(self) -> None:
        """Отказ от замены текста"""
        self.stop_dialogue(2)

    def processing_clipboard(self) -> None:
        """Обрабатываем буфер обмена"""
        clipboard_text = f.get_selection()

        # Если текст не выделен. Оставляем возможность вручную вставить его с помощью Ctrl_V
        if not clipboard_text:
            self.is_restore_clipboard = False

        self.show_original_text(clipboard_text)  # Отображаем обрабатываемый текст

    def change_original_text(self) -> None:
        """Отображаем преобразованный исходный текст"""
        logger.info(f"{C.LOGGER_TEXT_CHANGE} *'{self.txtEditSource.toPlainText()}'*")
        self.show_replacements_text(self.txtEditSource.toPlainText())

    def start_dialogue(self) -> None:
        """
        Начало диалога.
        :return: None
        """
        if not self.isHidden():  # Если диалог не закончен - новый не начинаем
            return

        window = f.get_window()  # Получаем активное окно операционной системы
        if window:
            window.activate()  # Активируем окно
            title = window.title
        else:
            title = C.TEXT_WINDOW_NOT_FOUND

        logger.info(f"{C.LOGGER_TEXT_START_DIALOGUE} - {title}")
        self.old_clipboard_text = (
            f.get_clipboard()
        )  # запоминаем буфер обмена для возможного дальнейшего восстановления
        self.is_restore_clipboard = True
        self.processing_clipboard()  # Обрабатываем буфер обмена
        self.setWindowFlag(
            Qt.WindowType.WindowStaysOnTopHint, True
        )  # Поднимаем окно диалога над всеми окнами
        self.show()  # Показываем окно
        # Делаем окно доступным для ввода с клавиатуры
        self.activateWindow()

    def stop_dialogue(self, command: int) -> None:
        """
        Выполняем команду, заданную в параметре.
        : command: (int) - Код команды закрытия диалога
        """

        # Обрабатываем команду
        match command:
            case 0:  # Выгрузка программы
                pass
            case 1:  # Заменяем выделенный текст
                f.replace_selected_text()
            case 2:  # Отказ от замены текста
                pass
            case _:  # Непредусмотренная команда
                logger.critical(f"{C.TEXT_CRITICAL_ERROR_1} {self.command =}")

        # Если буфер обмена не требуется для завершения действий Пользователя,
        # то восстанавливаем первоначальный буфер обмена
        if self.is_restore_clipboard:
            f.put_to_clipboard(self.old_clipboard_text)
            logger.info(
                f"{C.LOGGER_TEXT_RESTORED_CLIPBOARD} *'{self.old_clipboard_text}'*"
            )
        self.hide()  # Убираем окно с экрана
        logger.info(f"{C.LOGGER_TEXT_STOP_DIALOGUE}")
