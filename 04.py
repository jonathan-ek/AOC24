import re

from utils import get_input

def a():
    inp = get_input(4).strip()
    data = [[y for y in x] for x in inp.split('\n')]
    strings = []
    # horizontal
    for row in data:
        strings.append("".join(row))
    # vertical
    for i in range(len(data[0])):
        strings.append("".join([x[i] for x in data]))
    # diagonal 1
    for i in range(len(data) + len(data[0]) - 1):
        strings.append(
            "".join([data[x][y] for x in range(len(data)) for y in range(len(data[0])) if x + y == i]))
    # diagonal 2
    for i in range(-len(data[0]) + 1, len(data)):
        strings.append(
            "".join([data[x][y] for x in range(len(data)) for y in range(len(data[0])) if x - y == i]))
    total = 0
    for s in strings:
        res = len(re.findall(r'(?=XMAS|SAMX)', s))
        total += res
    print(total)


def b():
    inp = get_input(4).strip()
    data = [[y for y in x] for x in inp.split('\n')]
    ms = ['M', 'S']
    total = 0
    for i in range(len(data)-2):
        for j in range(len(data[0])-2):
            if (
                data[i + 1][j + 1] == 'A'
                and data[i][j] in ms
                and data[i][j + 2] in ms
                and data[i + 2][j] in ms
                and data[i + 2][j + 2] in ms
                and data[i][j] != data[i + 2][j + 2]
                and data[i][j + 2] != data[i + 2][j]
            ):
                total += 1
    print(total)




if __name__ == '__main__':
    # a()
    b()