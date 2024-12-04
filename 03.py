import re
from utils import get_input

def mult(x):
    return x[0] * x[1]

def a():
    inp = get_input(3).strip()
    instruction = 'mul'
    pattern = f'({instruction}\(\d{{1,3}},\d{{1,3}}\))'
    res = re.findall(pattern, inp, re.MULTILINE)
    total = sum([mult([int(y) for y in str(x).removeprefix(f"{instruction}(").removesuffix(")").split(',')]) for x in res])
    print(total)


def b():
    inp = get_input(3).strip()
    instruction = 'mul'
    pattern = f'(mul\(\d{{1,3}},\d{{1,3}}\)|do\(\)|don\'t\(\))'
    res = re.findall(pattern, inp, re.MULTILINE)
    inst = []
    do = True
    for r in res:
        if r == 'do()':
            do = True
        elif r == 'don\'t()':
            do = False
        elif do:
            inst.append(r)
    total = sum(
        [mult([int(y) for y in str(x).removeprefix(f"{instruction}(").removesuffix(")").split(',')]) for x in inst])

    print(total)


if __name__ == '__main__':
    # a()
    b()
