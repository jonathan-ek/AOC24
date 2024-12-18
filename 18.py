import heapq

from utils import get_input

def solve(pos, goal, falling_bytes, stop_at_goal=False):
    visited = {}
    heap = []
    heapq.heappush(heap, (0, pos))
    best = float('inf')
    has_res = False
    while heap:
        price, pos = heapq.heappop(heap)
        if price >= best:
            continue
        if pos in visited and visited[pos] <= price:
            continue
        visited[pos] = price
        if pos == goal:
            best = min(best, price)
            has_res = True
            if stop_at_goal:
                break
            continue
        new_pos = [
            (pos[0], pos[1] + 1),
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1)]
        for new_pos in new_pos:
            if new_pos not in falling_bytes and 0 <= new_pos[0] <= goal[0] and 0 <= new_pos[1] <= goal[1]:
                heapq.heappush(heap, (price + 1, new_pos))
    return best if has_res else None


def a():
    inp = [tuple([int(y) for y in x.split(',')]) for x in get_input(18).strip().split('\n')]
    pos = (0, 0)
    goal = (70, 70)
    falling_bytes = 1024
    # goal = (6, 6)
    # falling_bytes = 12
    # for y in range(goal[1]+1):
    #     for x in range(goal[0]+1):
    #         if (x, y) in inp[:falling_bytes]:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    print(solve(pos, goal, inp[:falling_bytes]))


def b():
    inp = [tuple([int(y) for y in x.split(',')]) for x in get_input(18).strip().split('\n')]
    pos = (0, 0)
    goal = (70, 70)
    low_bound = 1024
    high_bound = len(inp)
    while True:
        falling_bytes = (low_bound + high_bound) // 2
        res = solve(pos, goal, inp[:falling_bytes], True)
        if not res:
            high_bound = falling_bytes
        else:
            low_bound = falling_bytes
        if high_bound - low_bound <= 1:
            break
    breaking_byte = inp[high_bound-1]
    print(f"{breaking_byte[0]},{breaking_byte[1]}")


if __name__ == '__main__':
    a()
    b()