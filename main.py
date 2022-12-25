from len_sen_count import mid_sentence_len
from mid_word_len import mid_word_len
from all_words import all_words_statistic
from sep_line import get_coefs_for_line
from tests import test_an_author
from scraper import SYMBOLS_IN_FILE

import os
import matplotlib.pyplot as plt

FIRST_PATH = '/home/evarist/Рабочий стол/python/project/cheh'
SECOND_PATH = '/home/evarist/Рабочий стол/python/project/tolst'

FIRST_TEST_PATH = '/home/evarist/Рабочий стол/python/project/test_cheh'
SECOND_TEST_PATH = '/home/evarist/Рабочий стол/python/project/test_tolst'

SYMBOLS = SYMBOLS_IN_FILE


def _get_dirs(first_path:str, second_path:str) -> tuple:
    first_file_list = os.listdir(first_path)
    second_file_list = os.listdir(second_path)

    return (first_file_list, second_file_list)


def _get_mid_characteristics(file_list:list, path:str):
    mid_sentence_len_l = []
    mid_word_len_l = []
    for i in file_list:
        if i != 'source.txt':
            k1 = mid_sentence_len(f'{path}/{i}')
            if k1:
                mid_sentence_len_l.append(k1)
            k2 = mid_word_len(f'{path}/{i}')
            if k2:
                mid_word_len_l.append(k2)

    return mid_sentence_len_l, mid_word_len_l


def _get_matrix_with_mid_characteristics(mid_sentence_len_l:list, mid_word_len_l:list):
    matrix = []
    for i in range(min(len(mid_sentence_len_l), len(mid_word_len_l))):
        matrix.append([mid_sentence_len_l[i], mid_word_len_l[i]])
    return matrix


#returns an error (number of errors)
def test_all(data:list, line:list, must_be:str) -> float:
    errors = 0
    for point in data:
        if not test_an_author(point, line, must_be):
            errors += 1
    return round(1 - (errors / len(data)), 3)


def main():

    first_file_list, second_file_list = _get_dirs(FIRST_PATH, SECOND_PATH)

    mid_sentence_len_first, mid_word_len_first = _get_mid_characteristics(first_file_list, FIRST_PATH)
    mid_sentence_len_second, mid_word_len_second = _get_mid_characteristics(second_file_list, SECOND_PATH)
    
    
    plt.scatter(x = mid_sentence_len_first, y = mid_word_len_first, color = 'green')
    plt.scatter(x = mid_sentence_len_second, y = mid_word_len_second, color = 'red')
    

    matrix1 = _get_matrix_with_mid_characteristics(mid_sentence_len_first, mid_word_len_first)
    matrix2 = _get_matrix_with_mid_characteristics(mid_sentence_len_second, mid_word_len_second)

    line = get_coefs_for_line(matrix1, matrix2)
    print(f'{line} - line for studying choice')

    #tests
    first_file_list_test, second_file_list_test = _get_dirs(FIRST_TEST_PATH, SECOND_TEST_PATH)
    mid_sentence_len_first_test, mid_word_len_first_test = _get_mid_characteristics(first_file_list_test, FIRST_TEST_PATH)
    mid_sentence_len_second_test, mid_word_len_second_test = _get_mid_characteristics(second_file_list_test, SECOND_TEST_PATH)
    matrix1_test = _get_matrix_with_mid_characteristics(mid_sentence_len_first_test, mid_word_len_first_test)
    matrix2_test = _get_matrix_with_mid_characteristics(mid_sentence_len_second_test, mid_word_len_second_test)
    matrix1_test += matrix1
    matrix2_test += matrix2
    '''
    new_line = get_coefs_for_line(matrix1_test, matrix2_test)
    print(f'{new_line} - line for the testing choice')
    '''
    print(f"{test_all(matrix2_test, line, 'above')} - accuracy for Tolstoy (based)")
    print(f"{test_all(matrix1_test, line, 'under')} - accuracy for Chehov (based)")

    print(f"{test_all(matrix2_test, line, 'above')} - accuracy for Tolstoy (cringe)")
    print(f"{test_all(matrix1_test, line, 'under')} - accuracy for Chehov (cringe)")

    plt.scatter(x = mid_sentence_len_first_test, y = mid_word_len_first_test, color = 'blue')
    plt.scatter(x = mid_sentence_len_second_test, y = mid_word_len_second_test, color = 'orange')


    plt.plot([0, 25], [line[0] * 0 + line[1], line[0] * 25 + line[1]])
    ax = plt.gca()
    ax.set_xlabel("Средняя длина предложения (слов)")
    ax.set_ylabel("Средняя длина слова (символов)")
    plt.legend(['А.П.Чехов', 'Л.Н.Толстой', 'А.П.Чехов (тест)', 'Л.Н.Толстой (тест)'], loc='best')

    
    plt.savefig(f"/home/evarist/Рабочий стол/python/project/graphs/{SYMBOLS}.jpg")
    #plt.grid()
    plt.show()

if __name__ == '__main__':
    main()