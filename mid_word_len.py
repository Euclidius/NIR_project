import re
import os

def _get_words(file_name:str) -> list:
    with open(file_name) as f:
        data = f.read().lower()

    data = re.findall('[а-яё-]+', data, re.IGNORECASE)
    data = [i for i in data if i != '--']

    return data


def mid_word_len(file_name:str) -> float:
    if os.path.getsize(file_name) != 0:
        data = _get_words(file_name)
        word_counter = len(data)
        sum_word_len = sum([len(i) for i in data])

        return round(sum_word_len / word_counter, 3)


def main():
    path = '/home/evarist/Рабочий стол/python/new/cheh/c6.txt'
    print(round(mid_word_len(path), 3))

if __name__ == '__main__':
    main()