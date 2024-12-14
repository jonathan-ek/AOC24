import time
from PIL import Image

from utils import get_input


class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def pos_at(self, x, width, height):
        return (
            (self.position[0] + self.velocity[0] * x) % width,
            (self.position[1] + self.velocity[1] * x) % height
        )


def a():
    inp = get_input(14).strip().split('\n')
    robots = []
    for r in inp:
        p, v = r.split(' ')
        p = [int(x) for x in p[2:].split(',')]
        v = [int(x) for x in v[2:].split(',')]
        robots.append(Robot(p, v))
    # origo top left
    width = 101
    height = 103
    # width = 11
    # height = 7
    pos = [r.pos_at(100, width, height) for r in robots]
    for y in range(height):
        for x in range(width):
            if (x, y) in pos:
                # get number of robots at this position
                n = 0
                for p in pos:
                    if p == (x, y):
                        n += 1
                print(n, end='')
            else:
                print('.', end='')
        print()
    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0
    for p in pos:
        if p[0] < width // 2 and p[1] < height // 2:
            quadrant_1 += 1
        elif p[0] >= (width // 2) + 1 and p[1] < height // 2:
            quadrant_2 += 1
        elif p[0] < width // 2 and p[1] >= (height // 2) + 1:
            quadrant_3 += 1
        elif p[0] >= (width // 2) + 1 and p[1] >= (height // 2) + 1:
            quadrant_4 += 1
        else:
            pass
    print(quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4)


def b():
    inp = get_input(14).strip().split('\n')
    robots = []
    for r in inp:
        p, v = r.split(' ')
        p = [int(x) for x in p[2:].split(',')]
        v = [int(x) for x in v[2:].split(',')]
        robots.append(Robot(p, v))
    # origo top left
    width = 101
    height = 103
    # width = 11
    # height = 7
    for i in range(10000):
        img = Image.new('L', (width, height), 'black')
        pos = [r.pos_at(i, width, height) for r in robots]
        for y in range(height):
            for x in range(width):
                if (x, y) in pos:
                    # get number of robots at this position
                    n = 0
                    for p in pos:
                        if p == (x, y):
                            n += 1
                    img.putpixel((x, y), 255)
                else:
                    img.putpixel((x, y), 0)
        img.save(f'14/{i}.png')


if __name__ == '__main__':
    a()
    b()
