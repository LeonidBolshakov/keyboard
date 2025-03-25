"""Класс для замены символов, находящихся на одной клавише"""

from symbols import en_to_ru


class ReplaceText:
    def __init__(self):
        # Обратный словарь (русский -> английский)
        self.ru_to_en = {v: k for k, v in en_to_ru.items()}

    def swap_keyboard_layout(self, text_input: str) -> str:
        """
        Если символ на русском регистре, то заменяет его на английский, а если на английском регистре, то на русский
        :param text_input: (str) - Входной текст.
        :return: Текст с заменёнными символами.
        """
        text_output = []
        for symbol in text_input:
            if symbol in en_to_ru:
                text_output.append(en_to_ru[symbol])
            elif symbol in self.ru_to_en:
                text_output.append(self.ru_to_en[symbol])
            else:
                text_output.append(symbol)

        return "".join(text_output)
