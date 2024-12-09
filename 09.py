from utils import get_input


def a():
    inp = [int(x) for x in get_input(9).strip()]
    group = 0
    last_group = len(inp) // 2
    left_in_last_group = inp[-1]
    last_group_index = len(inp) - 1
    i = 0
    current_index = 0
    checksum = 0
    while True:
        for r in range(inp[i]):
            checksum += current_index * group
            current_index += 1
        i += 1
        free = inp[i]
        for r in range(free):
            while left_in_last_group == 0:
                last_group_index -= 2
                left_in_last_group = inp[last_group_index]
                last_group -= 1
                if last_group <= group:
                    left_in_last_group = 0
                    break
            if left_in_last_group == 0:
                break
            checksum += current_index * last_group
            left_in_last_group -= 1
            current_index += 1
        i += 1
        group += 1
        if last_group_index <= i:
            break
    for r in range(left_in_last_group):
        checksum += current_index * last_group
        current_index += 1
    print(checksum)

class Node:
    def __init__(self, value, group):
        self.value = value
        self.group = group



def b():
    inp = [int(x) for x in get_input(9).strip()]
    group = 0
    data = []
    for i in range(0, len(inp), 2):
        data.append(Node(inp[i], group))
        group += 1
        if i + 1 < len(inp):
            data.append(Node(inp[i + 1], []))

    for i in range(len(data)-1, 0, -1):
        if isinstance(data[i].group, int):
            for j in range(0, i):
                if data[j].value >= data[i].value and isinstance(data[j].group, list):
                    data[j].group.append(data[i])
                    data[j].value -= data[i].value
                    data[i] = Node(data[i].value, [])
                    break
        else:
            continue
    checksum = 0
    pos = 0
    for i in range(len(data)):
        if isinstance(data[i].group, list):
            for node in data[i].group:
                for r in range(node.value):
                    checksum += pos * node.group
                    pos += 1
            pos += data[i].value
        else:
            for r in range(data[i].value):
                checksum += pos * data[i].group
                pos += 1
    print(checksum)





if __name__ == '__main__':
    a()
    b()
