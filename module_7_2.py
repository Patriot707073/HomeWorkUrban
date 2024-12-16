def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    line_number = 1  # Счетчик для номеров строк
    for string in strings:
        byte_position = file.tell()  # Запоминаем текущую позицию в байтах перед записью строки
        file.write(string + '\n')  # Записываем строку в файл с переходом на новую строку
        strings_positions[(line_number, byte_position)] = string  # Заполняем словарь
        line_number += 1  # Увеличиваем номер строки

    file.close()  # Закрываем файл после завершения записи
    return strings_positions  # Возвращаем словарь строк и их позиций


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Выводим результат в читаемом формате
for elem in result.items():
    print(elem)
