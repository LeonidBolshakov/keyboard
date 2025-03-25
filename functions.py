"""Функции, не привязанные к классам"""

from time import sleep

from pyautogui import hotkey
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMessageBox, QPushButton, QApplication

from const import Const as C
import name


def press_ctrl(s: str) -> None:
    """
    Эмулировать нажатие клавиш Ctrl+символ.
    :param s: (str). Символ, нажимаемый вместе с Ctrl
    :return: None
    """
    hotkey("ctrl", s)

    # Ждём завершения команда Ctrl + {s}
    sleep(float(C.TIME_DELAY_CTRL))  # QTimer() отрабатывает некорректно.


def text_to_clipboard(text: str) -> None:
    """Записываем текст в буфер обмена"""
    clipboard = QApplication.clipboard()
    if clipboard:
        clipboard.setText(text)


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


def on_Cancel() -> None:
    """Выгружаем программу"""
    QApplication.quit()


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


def window_show() -> None:
    """
    Показ окна диалога.
    :return: None
    """
    window = name.window
    # Поднимаем окно над остальными окнами
    if window:
        # Поднимаем окно над всеми окнами
        window.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        window.processing_clipboard()  # Обрабатываем буфер обмена
        window.show()  # Выводим окно на экран
        # Делаем окно доступным для ввода с клавиатуры
        window.activateWindow()
    else:
        print("C.TEXT_CRITICAL_ERROR_2")


def window_hide() -> None:
    """Останавливаем работу с диалогом"""
    window = name.window
    rc = name.ret_code_dialogue
    # Обрабатываем ко
    match rc:
        case 0:  # Выгрузка программы
            pass
        case 1:  # Заменяем выделенный текст
            press_ctrl("v")  # Эмуляция Ctrl+v
        case 2:  # Отказ от замены текста
            pass
        case _:  # Непредусмотренная команда
            print(f"{C.TEXT_CRITICAL_ERROR_1} {name.ret_code_dialogue=}")

    if window:
        window.hide()  # Убираем окно с экрана
