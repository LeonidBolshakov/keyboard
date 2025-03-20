"""Класс для замены символов, находящихся на одной клавише"""

from symbols import en_to_ru


class ReplaceText:
    def __init__(self):
        # Подготовка таблицы для замены символов с английского регистра на русский
        self.translation_table = str.maketrans(en_to_ru)
        # Обратный словарь (русский -> английский)
        ru_to_en = {v: k for k, v in en_to_ru.items()}
        self.reverse_translation_table = str.maketrans(ru_to_en)

    def translate_text(self, text: str):
        """Заменяет символы с английского регистра на русский."""
        return text.translate(self.translation_table) if text else ""

    def reverse_translate_text(self, text: str):
        """Заменяет символы с русского регистра на английский."""
        return text.translate(self.reverse_translation_table) if text else ""
