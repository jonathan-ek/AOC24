from utils import get_input


def a():
    inp = get_input(13).split('\n\n')
    tokens = 0
    for d in inp:
        eq_a, eq_b, price = d.split('\n')
        eq_a_x, eq_a_y = [int(x[2:]) for x in eq_a.split(': ')[1].split(', ')]
        eq_b_x, eq_b_y = [int(x[2:]) for x in eq_b.split(': ')[1].split(', ')]
        price_x, price_y = [int(x[2:]) for x in price.split(': ')[1].split(', ')]
        y = (eq_a_y * price_x - eq_a_x * price_y) / (eq_b_x * eq_a_y - eq_b_y * eq_a_x)
        x = (price_x - eq_b_x * y) / eq_a_x
        if x.is_integer() and y.is_integer():
            if 0 <= x <= 100 and 0 <= y <= 100:
                tokens += int(x) * 3 + int(y)
    print(tokens)


def b():
    inp = get_input(13).split('\n\n')
    tokens = 0
    for d in inp:
        eq_a, eq_b, price = d.split('\n')
        eq_a_x, eq_a_y = [int(x[2:]) for x in eq_a.split(': ')[1].split(', ')]
        eq_b_x, eq_b_y = [int(x[2:]) for x in eq_b.split(': ')[1].split(', ')]
        price_x, price_y = [int(x[2:]) + 10000000000000 for x in price.split(': ')[1].split(', ')]
        y = (eq_a_y * price_x - eq_a_x * price_y) / (eq_b_x * eq_a_y - eq_b_y * eq_a_x)
        x = (price_x - eq_b_x * y) / eq_a_x
        if x.is_integer() and y.is_integer():
            if 0 <= x and 0 <= y:
                tokens += int(x) * 3 + int(y)
    print(tokens)


if __name__ == '__main__':
    a()
    b()
