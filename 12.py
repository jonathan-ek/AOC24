from utils import get_input


class Region:
    def __init__(self, region):
        self.region = region
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def is_in_region(self, region, point):
        if region == self.region:
            if point in self.points:
                return True
            return False
        else:
            return False

    def area(self):
        return len(self.points)

    def perimeter(self):
        perimeter = 0
        for p in self.points:
            for point in [
                (p[0] + 1, p[1]),
                (p[0] - 1, p[1]),
                (p[0], p[1] + 1),
                (p[0], p[1] - 1)
            ]:
                if point not in self.points:
                    perimeter += 1
        return perimeter

    def sides(self):
        sides = 0
        up = []
        down = []
        left = []
        right = []
        for p in self.points:
            if (p[0], p[1] - 1) not in self.points:
                up.append(p)
            if (p[0], p[1] + 1) not in self.points:
                down.append(p)
            if (p[0] - 1, p[1]) not in self.points:
                left.append(p)
            if (p[0] + 1, p[1]) not in self.points:
                right.append(p)
        up_sides = []
        for p in up:
            if p in [y for x in up_sides for y in x]:
                continue
            else:
                up_side = []
                for i in range(p[0], min([x[0] for x in up]) - 1, -1):
                    if (i, p[1]) in up:
                        up_side.append((i, p[1]))
                    else:
                        break
                for i in range(p[0], max([x[0] for x in up]) + 1):
                    if (i, p[1]) in up:
                        up_side.append((i, p[1]))
                    else:
                        break
                up_sides.append(up_side)
        sides += len(up_sides)
        down_sides = []
        for p in down:
            if p in [y for x in down_sides for y in x]:
                continue
            else:
                down_side = []
                for i in range(p[0], min([x[0] for x in down]) - 1, -1):
                    if (i, p[1]) in down:
                        down_side.append((i, p[1]))
                    else:
                        break
                for i in range(p[0], max([x[0] for x in down]) + 1):
                    if (i, p[1]) in down:
                        down_side.append((i, p[1]))
                    else:
                        break
                down_sides.append(down_side)
        sides += len(down_sides)
        left_sides = []
        for p in left:
            if p in [y for x in left_sides for y in x]:
                continue
            else:
                left_side = []
                for i in range(p[1], min([x[1] for x in left]) - 1, -1):
                    if (p[0], i) in left:
                        left_side.append((p[0], i))
                    else:
                        break
                for i in range(p[1], max([x[1] for x in left]) + 1):
                    if (p[0], i) in left:
                        left_side.append((p[0], i))
                    else:
                        break
                left_sides.append(left_side)
        sides += len(left_sides)
        right_sides = []
        for p in right:
            if p in [y for x in right_sides for y in x]:
                continue
            else:
                right_side = []
                for i in range(p[1], min([x[1] for x in right]) - 1, -1):
                    if (p[0], i) in right:
                        right_side.append((p[0], i))
                    else:
                        break
                for i in range(p[1], max([x[1] for x in right]) + 1):
                    if (p[0], i) in right:
                        right_side.append((p[0], i))
                    else:
                        break
                right_sides.append(right_side)
        sides += len(right_sides)
        return sides

    def value(self):
        return self.area() * self.perimeter()

    def discount_value(self):
        return self.area() * self.sides()

    def is_same_region(self, region):
        for point in region.points:
            if self.is_in_region(region.region, point):
                return True
        return False

    def join(self, region):
        self.points += region.points


def get_region(inp, point, points):
    for p in [
        (point[0] + 1, point[1]),
        (point[0] - 1, point[1]),
        (point[0], point[1] + 1),
        (point[0], point[1] - 1)
    ]:
        if p not in points and 0 <= p[0] < len(inp[0]) and 0 <= p[1] < len(inp):
            if inp[p[1]][p[0]] == inp[point[1]][point[0]]:
                points.add(p)
                get_region(inp, p, points)


def a():
    inp = [x for x in get_input(12).split('\n') if x]
    regions = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            added = False
            for region in regions:
                if region.is_in_region(inp[i][j], (j, i)):
                    added = True
                    break
            if not added:
                new_region = Region(inp[i][j])
                points = {(j, i)}
                get_region(inp, (j, i), points)
                for point in points:
                    new_region.add_point(point)
                regions.append(new_region)
    print(sum([region.value() for region in regions]))


def b():
    inp = [x for x in get_input(12).split('\n') if x]
    regions = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            added = False
            for region in regions:
                if region.is_in_region(inp[i][j], (j, i)):
                    added = True
                    break
            if not added:
                new_region = Region(inp[i][j])
                points = {(j, i)}
                get_region(inp, (j, i), points)
                for point in points:
                    new_region.add_point(point)
                regions.append(new_region)
    print(sum([region.discount_value() for region in regions]))


if __name__ == '__main__':
    # a()
    b()
