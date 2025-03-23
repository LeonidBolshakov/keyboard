"""Функции, не привязанные к классам"""

from pyautogui import hotkey
from time import sleep

from PyQt6.QtCore import Qt

from const import Const as C
import name


def press_ctrl(s: str) -> None:
    """
    Эмулировать нажатие клавиш Ctrl+символ.
    :param s: (str). Символ, нажимаемый вместе с Ctrl
    :return: None
    """
    hotkey("ctrl", s)
    sleep(C.DELAY_TIME_SECONDS)


def window_show() -> None:
    """
    Подготовительные действия и показ окна диалога.
    :return: None
    """
    window = name.window
    # Поднимаем окно над остальными окнами
    if window:
        window.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        window.processing_clipboard()  # Обрабатываем буфер обмена
        window.show()  # Выводим окно на экран
        # Делаем окно доступным для ввода с клавиатуры
        window.activateWindow()
    else:
        raise ValueError("C.TEXT_CRITICAL_ERROR_2")


def window_hide() -> None:
    """Обработка команд диалога после выполнения заданий Пользователя"""
    window = name.window
    rc = name.ret_code_dialogue

    match rc:
        case 0:  # Выгрузка программы
            pass
        case 1:  # Заменяем выделенный текст
            press_ctrl("v")  # Эмуляция Ctrl+v
        case 2:  # Отказ от замены текста
            pass
        case _:  # Непредусмотренная команда
            raise ValueError(f"{C.TEXT_CRITICAL_ERROR_1} {rc}")

    if window:
        window.hide()  # Убираем окно с экрана
