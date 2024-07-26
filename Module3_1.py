# Домашняя работа по уроку "Пространство имён"

count_calls_fn = 0 # Содержит кол-во вызовов функций

# stings - список строк для поиска в lists_to_search
strings = ["Дмитрий", "ЧЕЛЯБИНСК", "kldma", "АРБУЗ"]

# lists_to_search - списки для проверки вхождения строки из Strings в список
#                   из lists_to_search с индексом, соотствующим индексу строки из strings
lists_to_search = [["Сергей","Антон","Дмитрий","Валерий",],
                   ["Москва","Челябинск","Санкт-Питербург","Владивосток",],
                   ["kldma@rambler.ru","max@yandex.ru","vlad@mail.ru","ms_soft@gmail.com",],
                   ["абрикос", "дыня", "персик", "слива",]

                   ]
def count_calls(func):
    """Декоратор для подсчета количество вызовов функций,
       сохраняет результат в глобалльной переменной count_calls_fh"""
    def wrapper(*args, **kwargs):
        global count_calls_fn
        count_calls_fn += 1
        return func(*args, **kwargs)
    return wrapper

@count_calls
def string_info(string):
    """Получает строку и возвращает кортеж из длины строки, строки в верхнем регистре и
       строки в нижнем регистре"""
    string_data = (len(string), string.upper(), string.lower())

    return string_data

@count_calls
def is_contains(string, list_to_search):
    """Проверяет вхождение строки string в список list_to_search,
       возвращает True - если входит, False - если не входит,
       регистр не учитывается"""
    if any([string.lower() in string_.lower() for string_ in list_to_search]):
        return True
    return False

for i in range(0,len(strings)):
    print(string_info(strings[i]))
    print(is_contains(strings[i], lists_to_search[i]))

print(count_calls_fn)
