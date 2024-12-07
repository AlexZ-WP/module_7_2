from pprint import pprint

def custom_write(file_name, strings):

    """
    Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а
значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
    """
    file = open(file_name, 'a', encoding='utf-8')  # стараться открывать один раз для всего кода
    number_of_str = 0
    strings_positions = {}
    for i in strings:
        number_of_str += 1  # номер строки
        nb = file.tell()  # номер байта, сохраняем в переменную
        strings_positions[(number_of_str, nb)] = i
        file.write(i + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)

