"""Функции, не привязанные к классам"""

from time import sleep
import logging

logger = logging.getLogger(__name__)

from pyautogui import hotkey
import pygetwindow as gw
import pyperclip
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMessageBox, QPushButton, QApplication

from const import Const as C
from replacetext import ReplaceText


def press_ctrl(s: str, time_delay: int | float) -> None:
    """
    Эмулировать нажатие клавиш Ctrl+символ.
    :param s: (str). Символ, нажимаемый вместе с Ctrl
    :param time_delay: (int | float). Время задержки до и после нажатия клавиши
    :return: None
    """
    sleep(float(time_delay))
    hotkey(C.CTRL, s)
    logger.info(f"{C.LOGGER_TEXT_PRESS_CTRL}+{s}")

    # Ждём завершения команда Ctrl + {s}
    sleep(float(time_delay))  # QTimer() отрабатывает некорректно.


def put_clipboard(text: str) -> None:
    """Записываем текст в буфер обмена"""
    pyperclip.copy(text)


def making_button_settings(button: QPushButton, text: str, qss: str = "") -> None:
    """
    Настраивает свойства кнопки
    :param button: (QPushButton - Кнопка
    :param text: (str) - Текст кнопки
    :param qss: (str) - Стиль кнопки
    :return: None
    """
    button.setMinimumWidth(C.MIN_WIDTH_BUTTON)
    if qss:
        button.setStyleSheet(qss + C.QSS_BUTTON)
    button.setText(text)

    # Определяем, что если на кнопке установлен фокус, то при нажатии Enter она считается нажатой.
    button.setAutoDefault(True)


def show_message(
    message: str, show_seconds: int | float = 3, color: QColor = QColor("red")
) -> None:
    """
    Показать информационное сообщение.
    Сообщение можно убрать, нажав на кнопку ОК, клавишу Esc. Или оно само исчезнет через show_seconds секунд
    :param message: (str). Текст сообщения
    :param show_seconds: (int). Время в секундах, после которого сообщение автоматически убирается с экрана
    :param color: (QColor). Цвет сообщения
    :return: None
    """
    msg_box = QMessageBox()

    # Настраиваем окно сообщения
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.setStyleSheet(f"color: {color.name()};")
    # Находим кнопку OK и кликаем её с задержкой
    ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
    if ok_button:
        ok_button.clicked.connect(lambda: None)
        QTimer.singleShot(int(show_seconds * 1000), ok_button.click)

    msg_box.exec()


def replace_selected_text():
    """Заменяем выделенный текст"""
    text_from_clipboard = get_clipboard()
    press_ctrl("v", C.TIME_DELAY_CTRL_V)  # Эмуляция Ctrl+v
    logger.info(f"{C.LOGGER_TEXT_WRITE} *'{text_from_clipboard}'*")


def get_clipboard() -> str:
    """Возвращаем текст буфера обмена"""
    if QApplication.clipboard():
        return QApplication.clipboard().text()
    else:
        return ""


def get_replacement_option(text: str) -> str:
    """
    Находим вариант замены текста
    :param text: (str). Исходный текст
    :return: (str). Вариант замены
    """
    return ReplaceText().swap_keyboard_layout(text)


def get_selection() -> str:
    """
    Возвращаем выделенный текст
    :return: (str).
    """
    n = 0
    time_delay = 0
    while n < C.MAX_CLIPBOARD_READS:
        text_from_clipboard = _get_selection(time_delay)
        if text_from_clipboard:
            logger.info(f"{C.LOGGER_TEXT_BEEN_READ} *'{text_from_clipboard}'*")
            return text_from_clipboard
        logger.info(f"{C.LOGGER_TEXT_NO_BEEN_READ} {time_delay}")
        # Подготовка к следующей итерации
        time_delay += C.TIME_DELAY_CTRL_C
        n += 1

    logger.info(f"{C.LOGGER_TEXT_ERROR_READ}")
    return ""


def _get_selection(time_delay: float) -> str | None:
    """
    Считывает выделенный текст в буфер обмена.
    Если текст в буфер обмена не успел считаться, то возвращается C.EMPTY_TEXT
    :param time_delay: (float) - время задержки проверки после нажатия клавиш Ctrl+C
    :return: (str) Текст, считанный из
    """
    empty_text = C.EMPTY_TEXT
    put_clipboard(empty_text)
    press_ctrl("c", time_delay)
    text_from_clipboard = get_clipboard()

    return text_from_clipboard if text_from_clipboard != empty_text else None


def refocus_window() -> None:
    window = gw.getActiveWindow()
    if window:
        window.activate()
        sleep(0.3)
    else:
        logger.warning(C.LOGGER_TEXT_NO_ACTIVATE_WINDOW)
