from utils import get_input

def is_safe(report):
    sorted_report = sorted(report)
    if tuple(sorted_report) == tuple(report) or tuple(sorted_report[::-1]) == tuple(report):
        for i, x in enumerate(report):
            if i == len(report) - 1:
                break
            next_level = report[i+1]
            diff = abs(next_level - x)
            if 0 < diff <= 3:
                pass
            else:
                return False
        return True
    return False

def a():
    inp = get_input(2).strip()
    reports = [[int(y) for y in x.split(' ')] for x in inp.split('\n')]
    res = [is_safe(report) for report in reports]
    print(sum(res))

def b():
    inp = get_input(2).strip()
    reports = [[int(y) for y in x.split(' ')] for x in inp.split('\n')]
    res = []
    for report in reports:
        if is_safe(report):
            res.append(True)
        else:
            safe = False
            for i, level in enumerate(report):
                new_report = [x for j, x in enumerate(report) if i != j]
                if is_safe(new_report):
                    safe = True
                    break
            res.append(safe)
    print(sum(res))



if __name__ == '__main__':
    b()