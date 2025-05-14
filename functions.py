"""Функции, не привязанные к классам"""

from time import sleep
import ctypes
import sys
import logging

logger = logging.getLogger(__name__)

import pygetwindow as gw
import pyperclip
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor, QKeyEvent
from PyQt6.QtWidgets import QMessageBox, QPushButton
from PyQt6.QtCore import Qt
import keyboard

from const import Const as C
from replacetext import ReplaceText
from signals import signals


def press_ctrl(s: str, time_delay: int | float) -> None:
    """
    Эмулировать нажатие клавиш Ctrl+символ.
    :param s: (str). Символ, нажимаемый вместе с Ctrl
    :param time_delay: (int | float). Время после нажатия клавиши
    :return: None
    """
    press_key(s)
    sleep(time_delay)


def press_key(s: str):
    symbol = f"{C.CTRL}+{s}"
    keyboard.send(symbol)
    logger.info(f"   ->{symbol}")


def get_current_layout_id() -> int:
    """Получаем текущий layout_id"""
    hkl = ctypes.windll.user32.GetKeyboardLayout(0)
    return hkl & 0xFFFF


def set_layout_id(layout_id: int):
    """Устанавливаем раскладку по layout_id"""
    ctypes.windll.user32.PostMessageW(
        C.PM_HWND_BROADCAST,
        C.PM_WM_INPUTLANGCHANGEREQUEST,
        C.PM_FLAG_CHANGE,
        layout_id,
    )
    sleep(C.TIME_DELAY_SET_LAYOUT)


def put_to_clipboard(text: str) -> None:
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

    # Определяем, что если на кнопке установлен фокус, то при нажатии Enter она нажимается.
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
    # Находим9025138590 кнопку OK и кликаем её с задержкой
    ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
    if ok_button:
        ok_button.clicked.connect(lambda: None)
        QTimer.singleShot(int(show_seconds * 1000), ok_button.click)

    msg_box.exec()


def replace_selected_text():
    """Заменяем выделенный текст"""
    press_ctrl("v", C.TIME_DELAY_CTRL_V)  # Эмуляция Ctrl+v
    logger.info(f"{C.LOGGER_TEXT_WRITE} *'{get_clipboard()}'*")


def get_clipboard() -> str:
    """Возвращаем текст буфера обмена"""
    return pyperclip.paste()


def get_replacement_variant(text: str) -> str:
    """
    Находим вариант замены текста
    :param text: (str). Исходный текст
    :return: (str). Вариант замены
    """
    return ReplaceText().swap_keyboard_register(text)


def get_selection() -> str:
    """
    Возвращаем выделенный текст. В случае неудачи делаем несколько попыток считывания
    :return: (str).
    """
    time_delay = C.TIME_DELAY_CTRL_C
    for _ in range(C.MAX_CLIPBOARD_READS):
        text_from_clipboard = get_it_once(time_delay)
        if text_from_clipboard:
            return text_from_clipboard
        logger.info(f"{C.LOGGER_TEXT_NO_READ} {time_delay}")
        # Подготовка к следующей итерации
        time_delay += C.TIME_DELAY_CTRL_C

    logger.info(f"{C.LOGGER_TEXT_ERROR_READ}")
    return ""


def get_it_once(time_delay: float) -> str | None:
    """
    Считывает выделенный текст в буфер обмена.
    :param time_delay: (float) - время задержки проверки после нажатия клавиш Ctrl+C
    :return: (str) Текст, считанный из
    """

    pyperclip.copy("")
    press_ctrl("c", time_delay)
    return get_clipboard()


# noinspection PyProtectedMember
def get_window() -> gw._pygetwindow_win.Win32Window | None:
    """
    Возвращаем окно
    :return: (str). Заголовок окна
    """
    return gw.getActiveWindow()


def run_special_key(event: QKeyEvent) -> bool:
    """Обрабатываем нажатие горячих клавиш кнопок"""
    match event.key():
        case Qt.Key.Key_1:  # Заменять текст
            signals.on_Yes.emit()
        case Qt.Key.Key_Escape:  # Отказ от замены
            signals.on_No.emit()
        case Qt.Key.Key_2:  # Отказ от замены
            signals.on_No.emit()
        case Qt.Key.Key_3:  # Выгрузить программу
            signals.on_Cancel.emit()
        case _:
            return False

    return True


def init_logging():
    """Стартуем систему логирования"""
    logging.basicConfig(
        level=logging.INFO,
        filename=C.LOGGER_FILE_PATH,
        format=C.LOGGER_FORMAT,
    )


def parse_number(s: str) -> int | None:
    s = s.strip().lower()
    base = 16 if s.startswith("0x") else 10
    try:
        return int(s, base)
    except ValueError:
        logger.warning(f"{C.LOGGER_TEXT_ERROR_PARAM} - {s}")
        return None
