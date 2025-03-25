from pynput.keyboard import Listener

# Для определения кода клавиши. Запустите программу и нажмите нужную клавишу - программа выведет код клавиши.
# Например, для Windows,
# при нажатии на scr_lk будет выведено "Key.scroll_lock",
# Этот текст можно будет вставить в const.py. Key.scroll_lock - без кавычек.

with Listener(on_press=lambda key: print(f"Нажато: {key}")) as l:
    l.join()

# Уберите комментарии у следующих операторов и вставьте текст в конец модуля symbols.py.
# Выполнив программу Вы получите словарь замены символов в формате json.
# Далее в методе __init__ класса ReplaceText модуля replacetext.py можно вставить аналогичные операторы для чтения.
# В начале модуля надо будет убрать строчку from symbols import en_to_ru

# import json
# with open(file="config.json", mode="w") as f:
#     json.dump(en_to_ru, f)
