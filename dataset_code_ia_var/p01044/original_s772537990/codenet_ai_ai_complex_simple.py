from itertools import groupby, product, chain, islice
from functools import partial, reduce, lru_cache
from operator import itemgetter, attrgetter
import sys

class Simulator:
    def __init__(self, mp, width, height):
        self.mp = mp
        self.width = width
        self.height = height
        self.vec = [
            tuple(zip(*[[a, b] for a, b in [(1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (0, 1)]])),
            tuple(zip(*[[a, b] for a, b in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (0, 1)]]))
        ]
        self.checked = None
        self.erase_list = None

    def rotate(self, x, y):
        # Boundary check via all() and map
        if not all(map(lambda v: 0 < v[0] < v[1] - 1, zip([x, y], [self.width, self.height]))):
            return
        vec = self.vec[x & 1]
        indices = list(range(6))
        # Using reduce to get last color
        lx, ly = map(lambda u: u[-1], vec)
        last_color = reduce(lambda _, idx: self.mp[y + vec[1][idx]][x + vec[0][idx]], [5], None)
        # Multiple assignment in a loop via zip and reversed
        for i, j in zip(reversed(indices[1:]), reversed(indices[:-1])):
            self.mp[y + vec[1][i]][x + vec[0][i]] = self.mp[y + vec[1][j]][x + vec[0][j]]
        sx, sy = map(lambda u: u[0], vec)
        self.mp[y + sy][x + sx] = last_color

    def check(self):
        self.checked = [[False] * self.width for _ in range(self.height)]
        self.erase_list = []
        # List comprehension with side-effect wrapped in helper
        def mark_group(x, y):
            if self.checked[y][x] or self.mp[y][x] == ".": return
            self.checked[y][x] = True
            save = [(x, y)]
            self.search(x, y, save)
            if len(save) >= 3:
                self.erase_list.extend(save)
        list(map(lambda tpl: mark_group(*tpl), product(range(self.width), range(self.height))))

    def search(self, x, y, save):
        for dx, dy in zip(*self.vec[x & 1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.checked[ny][nx]:
                if self.mp[ny][nx] == self.mp[y][x]:
                    save.append((nx, ny))
                    self.checked[ny][nx] = True
                    self.search(nx, ny, save)

    def erase(self):
        # Elegant one-liner with map and itemgetter
        list(map(lambda p: self._erase_cell(*p), self.erase_list))

    def _erase_cell(self, x, y):
        self.mp[y][x] = '.'

    def fall(self):
        # Layered comprehension with obscure index cycles
        for y in range(1, self.height):
            for parity in (1, 0):
                xs = range(parity, self.width, 2)
                for x in xs:
                    if parity:
                        check_vec = ((-1, -1), (0, -1), (1, -1)) if x != self.width - 1 else ((-1, -1), (0, -1))
                    else:
                        check_vec = ((0, -1), (1, 0)) if x == 0 else ((-1, 0), (0, -1), (1, 0)) if x != self.width - 1 else ((-1, 0), (0, -1))
                    to_y = y
                    while to_y > 0 and all(0 <= x + dx < self.width for dx, _ in check_vec):
                        # Check all empty cell below via lambda
                        if all(self.mp[to_y + dy][x + dx] == '.' for dx, dy in check_vec):
                            to_y -= 1
                        else:
                            break
                    if to_y != y:
                        self.mp[to_y][x], self.mp[y][x] = self.mp[y][x], '.'

    def run(self):
        LIMIT = 100
        cnt = 0
        sentinel = object()
        while True:
            cnt += 1
            if cnt > LIMIT:
                (lambda x: print(x))('LIMIT_OVER')
                break
            self.fall()
            self.check()
            if not getattr(self, 'erase_list', sentinel): break
            if not self.erase_list: break
            self.erase()

    def print_mp(self):
        # Obscure use of reduce and chain.from_iterable to print
        def pr(line): print(''.join(line))
        list(map(lambda y: pr(self.mp[y]), reversed(range(self.height))))

h, w = map(int, next(iter(sys.stdin)).split())
mp = [list(line.rstrip()) for line in islice(sys.stdin, h)][::-1]
simulator = Simulator(mp, w, h)
simulator.run()
q = int(next(iter(sys.stdin)))
for _ in range(q):
    x, y = map(int, next(iter(sys.stdin)).split())
    simulator.rotate(x, y)
    simulator.run()
simulator.print_mp()