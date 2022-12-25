'''
Receive two matrixes with coords [[x1, y1], [x2, y2]] [[x3, y3], [x4, y4]]
and builds a line, which separate this coords
'''

def is_above_the_line(k, b, x, y) -> bool:
    return y > k * x + b


def is_under_the_line(k, b, x, y) -> bool:
    return y < k * x + b


def get_coefs_for_line(first_matrix:set, second_matrix:set) -> list:
    start_k = -10
    start_b = -10
    end_k = 10
    end_b = 10
    step_k = step_b = 0.01
    good_points = -9999999999
    max_good_points = -9999999999

    k = start_k
    b = start_b

    while k <= end_k:
        while b <= end_b:
            for i, j in zip(first_matrix, second_matrix):
                if k > 0:
                    if is_above_the_line(k, b, i[0], i[1]):
                        good_points += 1
                    if is_under_the_line(k, b, j[0], j[1]):
                        good_points += 1
                elif k < 0:
                    if is_under_the_line(k, b, i[0], i[1]):
                        good_points += 1
                    if is_above_the_line(k, b, j[0], j[1]):
                        good_points += 1

            if good_points > max_good_points:
                max_good_points = good_points
                best_result = [round(k, 6), round(b, 6)]
            
            good_points = 0

            b += step_b
        b = start_b
        k += step_k
    return best_result

def main():
    first_matrix = [[1, 2], [0.5, 5], [1.5, 2]]
    second_matrix = [[2, 3], [1, 4], [4, 3]]

    print(get_coefs_for_line(first_matrix, second_matrix))

if __name__ == '__main__':
    main()