"""Класс для прослушивания клавиатуры"""

from pynput.keyboard import Key, KeyCode, Listener

import functions as f
from const import Const as C


class Listen:

    @staticmethod
    def on_release(key: Key | KeyCode) -> None:
        """
        Обработка отпускания клавиши на клавиатуре.
        Если была отпущена клавиша "scr_lk", то выделенный текст копируется в буфер обмена
        и вызывается диалог PyQt6.
        По завершению PyQt6, при необходимости, производится вставка из буфера обмена
        :param key: (keyboard. KeyCode) Отпущенная клавиша.
        :return:    None
        """

        if key == C.KEY_BEGIN_DIALOGUE:
            # Эмуляция Ctrl+c
            f.press_ctrl("c")
            rc = f.init_PyQt6()  # Вызов диалога
            match rc:
                case 0:  # Закрытие окна средствами Windows
                    return  # Ничего не делаем
                case 1:
                    f.press_ctrl("v")  # Эмуляция Ctrl+v
                case 2:
                    return  # Ничего не делаем
                case 3:
                    # noinspection PyTypeChecker
                    return False  # Выгружаем программу
                case _:
                    raise ValueError(f"{C.TEXT_CRITICAL_ERROR} {rc}")

    def listen(self):
        """Прослушивание клавиатуры"""
        with Listener(on_press=None, on_release=self.on_release) as listener:
            listener.join()


if __name__ == "__main__":
    """Запуск программы"""
    listen = Listen()
    listen.listen()
