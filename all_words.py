import re

def _get_words(file_name:str) -> list:
    with open(file_name) as f:
        data = f.read().lower()

    data = re.findall('[а-яё-]+', data, re.IGNORECASE)
    data = [i for i in data if i != '--']

    return data

def all_words_statistic(file_name:str, words:dict = None) -> dict:

    if words is None:
        words = {}
    
    data = _get_words(file_name)

    for i in data:
        if i in words.keys():
            words[i] += 1;
        else:
            words.update({i:1})

    return words
    

def main():
    path = '/home/evarist/Рабочий стол/python/venv/new/source.txt'
    a = all_words_statistic(path)
    res = {key: val for key, val in sorted(a.items(), key = lambda ele: ele[1], reverse = True)}
    print(res)

if __name__ == '__main__':
    main()