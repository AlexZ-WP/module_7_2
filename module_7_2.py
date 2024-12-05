from pprint import pprint


def custom_write(file_name, strings):

    name = 'test.txt'
    for i in info:
        file = open(name, 'a')
        file.write(i + '\n')
        pprint(file.read())
        file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
