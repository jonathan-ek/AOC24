from utils import get_input


def a():
    inp = [[y for y in x] for x in get_input(8).strip().split('\n')]
    frequencies = {}
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '.':
                pass
            else:
                if inp[i][j] in frequencies:
                    frequencies[inp[i][j]].append((i, j))
                else:
                    frequencies[inp[i][j]] = [(i, j)]
    anti_nodes = set()
    for k, v in frequencies.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                node_1 = v[i]
                node_2 = v[j]
                diff = (node_2[0] - node_1[0], node_2[1] - node_1[1])
                possible_anti_nodes = [(node_1[0] - diff[0], node_1[1] - diff[1]), (node_2[0] + diff[0], node_2[1] + diff[1])]
                for an in possible_anti_nodes:
                    if 0 <= an[0] < len(inp) and 0 <= an[1] < len(inp[0]):
                        anti_nodes.add(an)
    print(len(anti_nodes))


def b():
    inp = [[y for y in x] for x in get_input(8).strip().split('\n')]
    frequencies = {}
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '.':
                pass
            else:
                if inp[i][j] in frequencies:
                    frequencies[inp[i][j]].append((i, j))
                else:
                    frequencies[inp[i][j]] = [(i, j)]
    anti_nodes = set()
    for k, v in frequencies.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                node_1 = v[i]
                node_2 = v[j]
                anti_nodes.add(node_1)
                anti_nodes.add(node_2)
                diff = (node_2[0] - node_1[0], node_2[1] - node_1[1])
                m = 1
                while True:
                    an = (node_1[0] - (diff[0] * m), node_1[1] - (diff[1] * m))
                    if an in [node_1, node_2]:
                        continue
                    if 0 <= an[0] < len(inp) and 0 <= an[1] < len(inp[0]):
                        anti_nodes.add(an)
                    else:
                        break
                    m += 1
                m = 1
                while True:
                    an = (node_1[0] + diff[0] * m, node_1[1] + diff[1] * m)
                    if 0 <= an[0] < len(inp) and 0 <= an[1] < len(inp[0]):
                        anti_nodes.add(an)
                    else:
                        break
                    m += 1
    print(len(anti_nodes))
    # for i in range(len(inp)):
    #     for j in range(len(inp[0])):
    #         if (i, j) in anti_nodes:
    #             print('#', end='')
    #         else:
    #             print(inp[i][j], end='')
    #     print()


if __name__ == '__main__':
    a()
    b()
