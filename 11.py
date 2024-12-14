from utils import get_input

def blink(number):
    if number == 0:
        return [1]
    if len(str(number)) % 2 == 0:
        r = len(str(number)) // 2
        return [int(str(number)[:r]), int(str(number)[r:])]
    return [number * 2024]

def a():
    inp = [int(x) for x in get_input(11).strip().split(' ')]
    for r in range(25):
        new_inp = []
        for i in range(len(inp)):
            new_inp += blink(inp[i])
        inp = new_inp
    print(len(inp))

def blink_b(number, count, new_inp):
    if number == 0:
        new_inp[1] = new_inp.get(1, 0) + count
    elif len(str(number)) % 2 == 0:
        r = len(str(number)) // 2
        nr_1 = int(str(number)[:r])
        nr_2 = int(str(number)[r:])
        new_inp[nr_1] = new_inp.get(nr_1, 0) + count
        new_inp[nr_2] = new_inp.get(nr_2, 0) + count
    else:
        new_inp[number * 2024] = new_inp.get(number * 2024, 0) + count


def b():
    inp = dict([(int(x), 1) for x in get_input(11).strip().split(' ')])
    last_len = 0
    for r in range(75):
        new_inp = {}
        for n, c in inp.items():
            blink_b(n, c, new_inp)
        inp = new_inp
    for n, c in inp.items():
        last_len += c
    print(last_len)


if __name__ == '__main__':
    a()
    b()