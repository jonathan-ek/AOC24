from functools import cmp_to_key

from utils import get_input

def a():
    inp = get_input(5).strip()
    rules, updates = inp.split('\n\n')
    rules = [[int(y) for y in x.split('|')] for x in rules.split('\n')]
    updates = [[int(y) for y in x.split(',')] for x in updates.split('\n')]
    total = 0
    for update in updates:
        valid = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                # Valid rule
                if update.index(rule[0]) > update.index(rule[1]):
                    valid = False
                    break
        if valid:
            total += update[len(update)//2]
    print(total)


def b():
    inp = get_input(5).strip()
    rules, updates = inp.split('\n\n')
    rules = [tuple([int(y) for y in x.split('|')]) for x in rules.split('\n')]
    updates = [[int(y) for y in x.split(',')] for x in updates.split('\n')]

    def cmp(x, y):
        return 1 if (x, y) in rules else (-1 if (y, x) in rules else 0)

    total = 0
    for update in updates:
        valid = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                # Valid rule
                if update.index(rule[0]) > update.index(rule[1]):
                    valid = False
                    break
        if not valid:
            new_update = sorted(update, key=cmp_to_key(cmp))
            total += new_update[len(update) // 2]
    print(total)

if __name__ == '__main__':
    # a()
    b()
