import re
from utils import get_input
GLOBAL_DO = True

def func_do():
    global GLOBAL_DO
    GLOBAL_DO = True

def func_dont():
    global GLOBAL_DO
    GLOBAL_DO = False

def func_mult(x):
    if GLOBAL_DO:
        return x[0] * x[1]
    return None

def a():
    inp = get_input(3).strip()
    instruction = 'mul'
    pattern = f'({instruction}\(\d{{1,3}},\d{{1,3}}\))'
    res = re.findall(pattern, inp, re.MULTILINE)
    total = sum([func_mult([int(y) for y in str(x).removeprefix(f"{instruction}(").removesuffix(")").split(',')]) for x in res])
    print(total)


def b():
    inp = get_input(3).strip()
    instructions = {
        'mul': {
            'pattern': r'mul\(\d{1,3},\d{1,3}\)',
            "args": {
                "pattern": r'\d{1,3},\d{1,3}',
                "func": lambda x: [int(y) for y in x.split(',')],
            },
            'func': func_mult
        },
        'do': {
            'pattern': r'do\(\)',
            'func': func_do
        },
        'dont': {
            'pattern': r'don\'t\(\)',
            'func': func_dont
        },
    }
    pattern = '|'.join([instructions[x]['pattern'] for x in instructions])
    res = re.findall(f"({pattern})", inp, re.MULTILINE)
    total = 0
    for r in res:
        for instruction in instructions.keys():
            if re.match(f"({instructions[instruction]['pattern']})", r):
                if 'args' in instructions[instruction]:
                    args = re.findall(instructions[instruction]['args']['pattern'], r)
                    args = instructions[instruction]['args']['func'](args[0])
                    func_res = instructions[instruction]['func'](args)
                    if func_res is not None:
                        total += func_res
                else:
                    func_res = instructions[instruction]['func']()
                    if func_res is not None:
                        total += func_res
                break

    print(total)


if __name__ == '__main__':
    # a()
    b()
