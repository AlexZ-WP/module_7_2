from pprint import pprint

def custom_write(file_name, strings):

    """
    Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а
значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
    """
    name = 'test.txt'
    for i in info:
        file = open(name, 'a')
        file.write(i + '\n')
        # pprint(file.read())
        # file.close()
    strings_positions = {}
    number_of_str = 0  # счётчик для строк
    file = open(file_name, 'r')
    file.tell()
    #print(file.tell())
    file.readline()
    number_of_str += 1
    #print(file.tell())

    for key in file_name:
        if key not in strings_positions:
            strings_positions[key] = (number_of_str, file.tell())
            break
        for value in file_name:
            strings_positions[key] = file.readline()

            return strings_positions
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)

# def custom_write(file_name, strings):
#
#     name = 'test.txt'
#     for i in info:
#         file = open(name, 'a')
#         file.write(i + '\n')
#         #pprint(file.read())
#         file.close()