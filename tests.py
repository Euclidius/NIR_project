def is_above_the_line(k, b, x, y) -> bool:
    return y > k * x + b


def is_under_the_line(k, b, x, y) -> bool:
    return y <= k * x + b


#line's equation is y = kx + b, k = line[0], b = line[1]
#must_be is in ('under', 'above')
def test_an_author(params:list, line:list, must_be:str) -> bool:
    k = line[0]
    b = line[1]
    if is_above_the_line(k, b, params[0], params[1]):
        return must_be == 'above'
    elif is_under_the_line(k, b, params[0], params[1]):
        return must_be == 'under'


def main():
    print(test_an_author([4.1, 13.5], [-0.0, 5.2], 'above'))

if __name__ == '__main__':
    main()
