import collections

from utils import get_input


def get_lists(inp):
    rows = inp.split('\n')
    list_1 = []
    list_2 = []
    for row in rows:
        d = [x for x in row.split(' ') if x != '']
        list_1.append(int(d[0]))
        list_2.append(int(d[1]))
    return list_1, list_2


def a():
    inp = get_input(1).strip()
    list_1, list_2 = get_lists(inp)
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    diff = 0
    for i in range(len(list_1)):
        diff += abs(list_1[i] - list_2[i])
    print(diff)


def b():
    inp = get_input(1).strip()
    list_1, list_2 = get_lists(inp)
    list_2_counts = collections.Counter(list_2)
    total = 0
    for i in list_1:
        if i in list_2_counts:
            total += i * list_2_counts[i]
    print(total)

if __name__ == '__main__':
    b()
