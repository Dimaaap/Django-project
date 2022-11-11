"""
def chunk_title(string_for_chunk: str):
    chunk_list = []
    split_string = string_for_chunk.split()
    split_string_more_3 = [i for i in split_string if len(i) >= 3]
    for index, word in enumerate(split_string_more_3):
        for word_index, _ in enumerate(word):
            chunk_list.append(word[word_index: word_index + 3])
    chunk_list = [i for i in chunk_list if len(i) >= 3]
    final_string = f'{" ".join(chunk_list)} {" ".join(split_string)}'
    return final_string


# print(chunk_title("Вивчаємо Python Том 1"))
# print(chunk_title('Програмуємо на Python Том 1'))
# print(chunk_title('Django Практика створення Web сайтів на Python'))
# print(chunk_title("PostgreSQL Основи мови SQL"))
# print(chunk_title("Укус Python"))
# print(chunk_title("Програмування на Python Том 1"))
# print(chunk_title("Програмуємо на Python"))
# print(chunk_title("Чистий код Створення аналіз та рефакторинг"))
# print(chunk_title("Секрети Python 59 рекомендацій з написання ефективного коду"))
# print(chunk_title("Використання Docker"))
"""


def chunk_title(string_for_chunk: str):
    chunk_list = []
    split_string = string_for_chunk.split()
    split_string_more_3_letters = [i for i in split_string if len(i) >= 3]
    for index, word in enumerate(split_string_more_3_letters):
        for word_index, _ in enumerate(word):
            chunk_list.append(word[:word_index])
    chunk_list = [i for i in chunk_list if len(i) >= 3]
    return ' '.join(chunk_list) + ' ' + ' '.join(split_string)

# print(chunk_title('Програмування на Python Том 1'))
# print(chunk_title('Вивчаємо Python Том 1'))
# print(chunk_title('PostgreSQL Основи мови SQL'))
# print(chunk_title('Укус Python'))
# print(chunk_title('Django Практика створення Web-сайтів на Python'))
# print(chunk_title("Програмуємо на Python"))
# print(chunk_title("Чистий код Створення,аналіз та рефакторинг"))
# print(chunk_title("Секрети Python 59 рекомендацій з написання ефективного коду"))
# print(chunk_title("Використання Docker"))
# print(chunk_title("Грокаємо алгоритми"))
