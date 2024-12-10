from utils import get_input

class Node:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value
        self.adjacent = []
        self.start_nodes = set()

    def __repr__(self):
        return f'Node({self.pos}, {self.value}, {self.start_nodes}, {self.adjacent})'

def append_start_nodes(current_node, start_node):
    for node in current_node.adjacent:
        node.start_nodes.add(start_node)
        append_start_nodes(node, start_node)

def a():
    inp = [[Node((x, y), int(val)) for x, val in enumerate(row)] for y, row in enumerate(get_input(10).strip().split('\n'))]
    start_nodes = []
    end_nodes = []
    for row in inp:
        for node in row:
            if node.value == 0:
                start_nodes.append(node)
            if node.value == 9:
                end_nodes.append(node)
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (
                    0 <= node.pos[0] + i < len(inp)
                    and 0 <= node.pos[1] + j < len(inp[0])
                    and node.value + 1 == inp[node.pos[1] + j][node.pos[0] + i].value
                ):
                    node.adjacent.append(inp[node.pos[1] + j][node.pos[0] + i])
    for start_node in start_nodes:
        append_start_nodes(start_node, start_node)
    total = 0
    for end_node in end_nodes:
        total += len(end_node.start_nodes)
    print(total)



class NodeB:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value
        self.adjacent = []
        self.start_nodes = []

    def __repr__(self):
        return f'Node({self.pos}, {self.value}, {self.start_nodes}, {self.adjacent})'

def append_start_nodes_b(current_node, start_node):
    for node in current_node.adjacent:
        node.start_nodes.append(start_node)
        append_start_nodes_b(node, start_node)

def b():
    inp = [[NodeB((x, y), int(val)) for x, val in enumerate(row)] for y, row in
           enumerate(get_input(10).strip().split('\n'))]
    start_nodes = []
    end_nodes = []
    for row in inp:
        for node in row:
            if node.value == 0:
                start_nodes.append(node)
            if node.value == 9:
                end_nodes.append(node)
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (
                        0 <= node.pos[0] + i < len(inp)
                        and 0 <= node.pos[1] + j < len(inp[0])
                        and node.value + 1 == inp[node.pos[1] + j][node.pos[0] + i].value
                ):
                    node.adjacent.append(inp[node.pos[1] + j][node.pos[0] + i])
    for start_node in start_nodes:
        append_start_nodes_b(start_node, start_node)
    total = 0
    for end_node in end_nodes:
        total += len(end_node.start_nodes)
    print(total)


if __name__ == '__main__':
    a()
    b()
