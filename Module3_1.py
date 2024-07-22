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
def count_calls():
    """Подсчитывает количество вызовов функций и
       сохраняет в глобалльной переменной count_calls_fh"""
    global count_calls_fn
    count_calls_fn +=1

def string_info(string):
    """Получает строку и возвращает кортеж из длины строки, строки в верхнем регистре и
       строки в нижнем регистре"""
    count_calls()
    string_data = (len(string), string.upper(), string.lower())

    return string_data

def is_contains(string, list_to_search):
    """Проверяет вхождение строки string в список list_to_search,
       возвращает True - если входит, False - если не входит,
       регистр не учитывается"""
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower():
            return True
    return False

for i in range(0,len(strings)):
    print(string_info(strings[i]))
    print(is_contains(strings[i], lists_to_search[i]))

print(count_calls_fn)
