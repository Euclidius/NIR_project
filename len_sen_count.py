"""
Going threw the letters if ' ', counter += 1, if '.', sen_counter += 1
"""
import re
import os

def _get_words(file_name:str) -> list:
    with open(file_name) as f:
        data = f.read().lower()

    data = re.findall('[а-я.?!ё-]+', data, re.IGNORECASE)
    data = [i for i in data if i != '--']

    return data


def mid_sentence_len(file_name:str) -> float:
    if os.path.getsize(file_name) != 0:
        data = _get_words(file_name)
        
        sentence_counter = 0
        for i in data:
            if i[-1] in ('.', '!', '?'):
                sentence_counter += 1

        total_words = len(data)

        return round(total_words / sentence_counter, 3)

def main():
    pass


if __name__ == '__main__':
    main()