from utils import get_input


def a():
    inp = get_input(6).strip()
    data = [[y for y in x] for x in inp.split('\n')]
    obstacles = set()
    directions = ['^', '>', 'v', '<']
    direction = 0
    pos = (0, 0)
    visited = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                obstacles.add((i, j))
            elif data[i][j] in directions:
                pos = (i, j)
                direction = directions.index(data[i][j])
    while True:
        if direction == 0:
            next_pos = (pos[0] - 1, pos[1])
        elif direction == 1:
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 2:
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 3:
            next_pos = (pos[0], pos[1] - 1)
        else:
            raise Exception("Invalid direction")
        if next_pos in obstacles:
            direction = (direction + 1) % 4
        else:
            pos = next_pos

        if pos[0] < 0 or pos[0] >= len(data) or pos[1] < 0 or pos[1] >= len(data[0]):
            break
        else:
            visited.add(pos)
    print(len(visited))


def b():
    inp = get_input(6).strip()
    data = [[y for y in x] for x in inp.split('\n')]
    base_obstacles = set()
    directions = ['^', '>', 'v', '<']
    direction = 0
    pos = (0, 0)
    new_obstacles = set()
    possible_new_obstacles = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                base_obstacles.add((i, j))
            elif data[i][j] in directions:
                pos = (i, j)
                direction = directions.index(data[i][j])
            else:
                possible_new_obstacles.add((i, j))
    start_pos = pos
    start_direction = direction
    for idx, obs in enumerate(possible_new_obstacles):
        print(f"\rProcessing {idx}/{len(possible_new_obstacles)}", end="")
        pos = start_pos
        direction = start_direction
        obstacles = base_obstacles.copy()
        obstacles.add(obs)
        visited = set()
        while True:
            if direction == 0:
                next_pos = (pos[0] - 1, pos[1])
            elif direction == 1:
                next_pos = (pos[0], pos[1] + 1)
            elif direction == 2:
                next_pos = (pos[0] + 1, pos[1])
            elif direction == 3:
                next_pos = (pos[0], pos[1] - 1)
            else:
                raise Exception("Invalid direction")
            if next_pos in obstacles:
                direction = (direction + 1) % 4
            else:
                pos = next_pos

            if pos[0] < 0 or pos[0] >= len(data) or pos[1] < 0 or pos[1] >= len(data[0]):
                break
            else:
                pos_dir = (pos[0], pos[1], direction)
                if pos_dir in visited:
                    new_obstacles.add(obs)
                    break
                visited.add(pos_dir)
    print()
    print(len(new_obstacles))


if __name__ == '__main__':
    a()
    b()