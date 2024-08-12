from pprint import pprint
def custom_write(file_name, strings):
    q = 0
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for i in strings:
        q += 1
        a = file.tell()
        file.write(i + '\n')
        strings_positions[q, a] = i
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


