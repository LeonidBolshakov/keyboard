"""Класс для замены символов, находящихся на одной клавише"""

from symbols import en_to_ru


class ReplaceText:
    def __init__(self):
        # Подготовка таблицы для замены символов с английского регистра на русский
        self.translation_table = str.maketrans(en_to_ru)
        # Обратный словарь (русский -> английский)
        self.ru_to_en = {v: k for k, v in en_to_ru.items()}
        self.reverse_translation_table = str.maketrans(self.ru_to_en)

    def translate_text(self, text: str) -> str:
        """
        Заменяет символы с английского регистра на русский.
                :param text: (str) - Входной текст.
        :return: Текст с заменёнными символами.
        """
        return text.translate(self.translation_table) if text else ""

    def reverse_translate_text(self, text: str) -> str:
        """
        Заменяет символы с русского регистра на английский.
                :param text: (str) - Входной текст.
        :return: Текст с заменёнными символами.
        """
        return text.translate(self.reverse_translation_table) if text else ""

    def swap_keyboard_layout(self, text_in: str) -> str:
        """
        Если символ на русском регистре, то заменяет его на английский, а если на английском регистре, то на русский
        :param text_in: (str) - Входной текст.
        :return: Текст с заменёнными символами.
        """
        text_out = []
        for symbol in text_in:
            if symbol in en_to_ru:
                text_out.append(en_to_ru[symbol])
            elif symbol in self.ru_to_en:
                text_out.append(self.ru_to_en[symbol])
            else:
                text_out.append(symbol)

        return "".join(text_out)
