import heapq
from utils import get_input


class Maze:
    def __init__(self, inp_map):
        self.inp_map = inp_map
        self.width = None
        self.height = None
        self.walls = []
        self.position = None
        self.direction = 90
        self.goal = None
        self.read_map()

    def read_map(self):
        d = self.inp_map.split('\n')
        self.width = len(d[0])
        self.height = len(d)
        for y, i in enumerate(d):
            for x, c in enumerate(i):
                if c == 'S':
                    self.position = (x, y)
                if c == 'E':
                    self.goal = (x, y)
                if c == '#':
                    self.walls.append((x, y))

    def print_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.position:
                    print('S', end='')
                elif (x, y) == self.goal:
                    print('E', end='')
                elif (x, y) in self.walls:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    @staticmethod
    def move(pos, direction):
        x, y = pos
        if direction == 0:
            return x, y - 1
        if direction == 90:
            return x + 1, y
        if direction == 180:
            return x, y + 1
        if direction == 270:
            return x - 1, y

    def solve(self):
        visited = {}
        heap = []
        heapq.heappush(heap, (0, self.position, self.direction))
        best = float('inf')
        while heap:
            price, pos, direction = heapq.heappop(heap)
            if price >= best:
                continue
            key = (pos, direction)
            if key in visited and visited[key] < price:
                continue
            visited[key] = price
            if pos == self.goal:
                best = min(best, price)
                continue
            # move forward
            new_pos = self.move(pos, direction)
            if new_pos not in self.walls:
                heapq.heappush(heap, (price + 1, new_pos, direction))
            # turn left
            heapq.heappush(heap, (price + 1000, pos, (direction - 90) % 360))
            # turn right
            heapq.heappush(heap, (price + 1000, pos, (direction + 90) % 360))
        print(best)

    def solve_b(self):
        visited = {}
        best_paths = {}
        heap = []
        heapq.heappush(heap, (0, self.position, self.direction, []))
        best = float('inf')
        paths = []
        while heap:
            price, pos, direction, path = heapq.heappop(heap)
            if price > best:
                continue
            key = (pos, direction)
            if key in visited and visited[key] < price:
                continue
            if key in visited and visited[key] == price:
                best_paths[key].append(path)
            else:
                visited[key] = price
                best_paths[key] = [path]
            if pos == self.goal:
                if price == best:
                    paths.append(path)
                if price < best:
                    best = price
                    paths = [path]
                continue
            # move forward
            new_pos = self.move(pos, direction)
            if new_pos not in self.walls:
                heapq.heappush(heap, (price + 1, new_pos, direction, [*path, new_pos]))
            # turn left
            heapq.heappush(heap, (price + 1000, pos, (direction - 90) % 360, [*path]))
            # turn right
            heapq.heappush(heap, (price + 1000, pos, (direction + 90) % 360, [*path]))
        print(len(set([x for y in paths for x in y])) + 1)


def a():
    inp = get_input(16).strip()
    maze = Maze(inp)
    maze.solve()


def b():
    inp = get_input(16).strip()
    maze = Maze(inp)
    maze.solve_b()


if __name__ == '__main__':
    a()
    b()
