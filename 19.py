from collections.abc import Iterable

def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x
from utils import get_input

def can_make_pattern(design, patterns):
    tokens = ['']
    while True:
        new_token = []
        for token in tokens:
            for pattern in patterns:
                new_pattern = f"{token}{pattern}"
                if design.startswith(new_pattern):
                    if new_pattern == design:
                        return True
                    new_token.append(new_pattern)
        if not new_token:
            return False
        tokens = new_token


def a():
    patterns, designs = get_input(19).strip().split('\n\n', 1)
    patterns = patterns.split(', ')
    designs = designs.split('\n')
    tokens = ['']
    found_patterns = []
    i = 0
    visited = set()
    while True:
        new_token = []
        for token in tokens:
            for pattern in patterns:
                new_pattern = f"{token}{pattern}"
                if new_pattern in visited:
                    continue
                visited.add(new_pattern)
                for design in designs:
                    if design.startswith(new_pattern):
                        if new_pattern == design:
                            found_patterns.append(new_pattern)
                        else:
                            new_token.append(new_pattern)
        new_designs = designs.copy()
        for d in designs:
            if d in found_patterns:
                new_designs.remove(d)
                continue
            has_start = False
            for p in new_token:
                if d.startswith(p):
                    has_start = True
                    break
            if not has_start:
                new_designs.remove(d)
        designs = new_designs
        print(len(designs))
        print(len(new_token))

        if not new_token:
            break
        i += 1
        tokens = list(set(new_token))

    print(len(found_patterns))


class NestedCounter:
    def __init__(self, counter=None):
        self.counter = [counter] if counter else []
        self.cached = None

    def __add__(self, other):
        self.counter.append(other)
        return self

    def __int__(self):
        if len(self.counter) == 0:
            return 1
        if self.cached is not None:
            return self.cached
        self.cached = sum([int(x) for x in self.counter])
        return self.cached

def b():
    patterns, designs = get_input(19).strip().split('\n\n', 1)
    patterns = patterns.split(', ')
    designs = designs.split('\n')
    tokens = ['']
    found_patterns = []
    visited = {'': 1}
    while True:
        new_token = []
        for token in tokens:
            for pattern in patterns:
                new_pattern = f"{token}{pattern}"
                if new_pattern in visited:
                    visited[new_pattern] += visited[token]
                    continue
                visited[new_pattern] = NestedCounter(visited[token])
                for design in designs:
                    if design.startswith(new_pattern):
                        if new_pattern == design:
                            found_patterns.append(new_pattern)
                        else:
                            new_token.append(new_pattern)
        new_designs = designs.copy()
        for d in designs:
            has_start = False
            for p in new_token:
                if d.startswith(p):
                    has_start = True
                    break
            if not has_start:
                new_designs.remove(d)
        designs = new_designs
        tokens = list(set(new_token))
        print(len(designs))
        print(len(new_token))

        if not new_token:
            break
    # print([(p, int(visited[p])) for p in found_patterns])
    print(sum([int(visited[p]) for p in found_patterns]))



if __name__ == '__main__':
    # a()
    b()
