class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем переданные файлы

    def get_all_words(self):
        all_words = {}  # Словарь для хранения слов из файлов
        punctuation = ",.!?;:-"  # Пунктуация, которую нужно удалить

        for file_name in self.file_names:
            words_in_file = []  # Список для хранения слов из одного файла

            # Открываем файл
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()  # Приводим строку в нижний регистр

                    # Убираем пунктуацию
                    for char in punctuation:
                        line = line.replace(char, ' ')  # Заменяем пунктуацию на пробелы

                    words_in_file.extend(line.split())  # Разбиваем строку на слова по пробелам и добавляем их в список

            all_words[file_name] = words_in_file  # Сохраняем слова из этого файла в словарь

        return all_words

    def find(self, word):
        word = word.lower()  # Игнорируем регистр
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            if word in words:  # Если слово найдено
                position = words.index(word) + 1  # Находим первое вхождение
                result[file_name] = position  # Записываем в словарь

        return result

    def count(self, word):
        word = word.lower()  # Игнорируем регистр
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            count = words.count(word)  # Подсчитываем количество вхождений
            result[file_name] = count  # Записываем в словарь

        return result
