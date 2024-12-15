from utils import get_input


class Game:
    def __init__(self, inp_map):
        self.inp_map = inp_map
        self.width = None
        self.height = None
        self.boxes = []
        self.walls = []
        self.position = None
        self.read_map()

    def read_map(self):
        d = self.inp_map.split('\n')
        self.width = len(d[0])
        self.height = len(d)
        for y, i in enumerate(d):
            for x, c in enumerate(i):
                if c == '@':
                    self.position = (x, y)
                if c == 'O':
                    self.boxes.append((x, y))
                if c == '#':
                    self.walls.append((x, y))

    def print_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.position:
                    print('@', end='')
                elif (x, y) in self.boxes:
                    print('O', end='')
                elif (x, y) in self.walls:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    def move_box(self, box, d):
        if d == '<':
            new_pos = (box[0] - 1, box[1])
        elif d == '>':
            new_pos = (box[0] + 1, box[1])
        elif d == '^':
            new_pos = (box[0], box[1] - 1)
        elif d == 'v':
            new_pos = (box[0], box[1] + 1)
        else:
            return False
        if new_pos in self.walls:
            return False
        if new_pos in self.boxes:
            res = self.move_box(new_pos, d)
            if not res:
                return False
        self.boxes.remove(box)
        self.boxes.append(new_pos)
        return True

    def move(self, d):
        if d == '<':
            new_pos = (self.position[0] - 1, self.position[1])
        elif d == '>':
            new_pos = (self.position[0] + 1, self.position[1])
        elif d == '^':
            new_pos = (self.position[0], self.position[1] - 1)
        elif d == 'v':
            new_pos = (self.position[0], self.position[1] + 1)
        else:
            return
        if new_pos in self.walls:
            return
        if new_pos in self.boxes:
            res = self.move_box(new_pos, d)
            if not res:
                return
        self.position = new_pos

    def gps(self):
        return sum([100 * y + x for x, y in self.boxes])


def a():
    inp_map, inst = get_input(15).strip().split('\n\n')
    game = Game(inp_map)
    # game.print_map()
    for i in inst:
        game.move(i)
        # game.print_map()
    print(game.gps())


class GameB:
    def __init__(self, inp_map):
        self.inp_map = inp_map
        self.width = None
        self.height = None
        self.boxes = []
        self.walls = []
        self.position = None
        self.read_map()

    def read_map(self):
        d = self.inp_map.split('\n')
        self.width = len(d[0])
        self.height = len(d)
        for y, i in enumerate(d):
            for x, c in enumerate(i):
                if c == '@':
                    self.position = (x * 2, y)
                if c == 'O':
                    self.boxes.append(((x * 2, y), (x * 2 + 1, y)))
                if c == '#':
                    self.walls.append(((x * 2, y), (x * 2 + 1, y)))

    def print_map(self):
        for y in range(self.height):
            for x in range(self.width * 2):
                if (x, y) == self.position:
                    print('@', end='')
                elif ((x, y), (x + 1, y)) in self.boxes:
                    print('[', end='')
                elif ((x - 1, y), (x, y)) in self.boxes:
                    print(']', end='')
                elif ((x, y), (x + 1, y)) in self.walls:
                    print('#', end='')
                elif ((x - 1, y), (x, y)) in self.walls:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    def move_box(self, box, d):
        if (box, (box[0] + 1, box[1])) in self.boxes:
            whole_box = (box, (box[0] + 1, box[1]))
        elif ((box[0] - 1, box[1]), box) in self.boxes:
            whole_box = ((box[0] - 1, box[1]), box)
        else:
            return False

        if d == '<':
            new_pos = (whole_box[0][0] - 1, whole_box[0][1]), (whole_box[1][0] - 1, whole_box[1][1])
        elif d == '>':
            new_pos = (whole_box[0][0] + 1, whole_box[0][1]), (whole_box[1][0] + 1, whole_box[1][1])
        elif d == '^':
            new_pos = (whole_box[0][0], whole_box[0][1] - 1), (whole_box[1][0], whole_box[1][1] - 1)
        elif d == 'v':
            new_pos = (whole_box[0][0], whole_box[0][1] + 1), (whole_box[1][0], whole_box[1][1] + 1)
        else:
            return False
        for p in new_pos:
            if p in [y for x in self.walls for y in x]:
                return False
            if p in [y for x in [z for z in self.boxes if z != whole_box] for y in x]:
                self.move_box(p, d)
        self.boxes.remove(whole_box)
        self.boxes.append(new_pos)

    def can_move_box(self, box, d):
        if (box, (box[0] + 1, box[1])) in self.boxes:
            whole_box = (box, (box[0] + 1, box[1]))
        elif ((box[0] - 1, box[1]), box) in self.boxes:
            whole_box = ((box[0] - 1, box[1]), box)
        else:
            return False

        if d == '<':
            new_pos = (whole_box[0][0] - 1, whole_box[0][1]), (whole_box[1][0] - 1, whole_box[1][1])
        elif d == '>':
            new_pos = (whole_box[0][0] + 1, whole_box[0][1]), (whole_box[1][0] + 1, whole_box[1][1])
        elif d == '^':
            new_pos = (whole_box[0][0], whole_box[0][1] - 1), (whole_box[1][0], whole_box[1][1] - 1)
        elif d == 'v':
            new_pos = (whole_box[0][0], whole_box[0][1] + 1), (whole_box[1][0], whole_box[1][1] + 1)
        else:
            return False
        for p in new_pos:
            if p in [y for x in self.walls for y in x]:
                return False
            if p in [y for x in [z for z in self.boxes if z != whole_box] for y in x]:
                if not self.can_move_box(p, d):
                    return False
        return True

    def move(self, d):
        if d == '<':
            new_pos = (self.position[0] - 1, self.position[1])
        elif d == '>':
            new_pos = (self.position[0] + 1, self.position[1])
        elif d == '^':
            new_pos = (self.position[0], self.position[1] - 1)
        elif d == 'v':
            new_pos = (self.position[0], self.position[1] + 1)
        else:
            return
        if new_pos in [y for x in self.walls for y in x]:
            return
        if new_pos in [y for x in self.boxes for y in x]:
            res = self.can_move_box(new_pos, d)
            if not res:
                return
            else:
                self.move_box(new_pos, d)
        self.position = new_pos

    def gps(self):
        return sum([100 * y + x for ((x, y), _) in self.boxes])


def b():
    inp_map, inst = get_input(15).strip().split('\n\n')
    game = GameB(inp_map)
    # game.print_map()
    for i in inst:
        game.move(i)
        # game.print_map()
    print(game.gps())


if __name__ == '__main__':
    a()
    b()
