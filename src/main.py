import re
def clear_names(file_name: str) -> list:
    """ Функция для очистки имен от лишних символов"""
    new_names_list = []
    with open("c:\\python\\homeWork_9_2\\data\\" + file_name, encoding='utf-8') as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ""
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)

    return new_names_list

def is_cirillic(name_item: str) -> bool:
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.search("[а-яА-Я]", name_item))

def filter_russian_names(names_list: list) -> list:
    """ Фильтрация имен, написанных на русском яэыке"""
    new_names_list = []
    for name_item in names_list:
        if is_cirillic(name_item):
            new_names_list.append(name_item)
    return new_names_list


def save_to_file(file_name: str, data: str) -> None:
    """Сохраняет данные в файл"""
    with open("c:\\python\\homeWork_9_2\\data\\" + file_name, "w") as names_file:
        names_file.write(data)

if __name__ == '__main__':
    cleared_name = clear_names("names.txt")

    filtered_names = filter_russian_names(cleared_name)
    save_to_file("russian_names.txt","\n ".join(filtered_names))