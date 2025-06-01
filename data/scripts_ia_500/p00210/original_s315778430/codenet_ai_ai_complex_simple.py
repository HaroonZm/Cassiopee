from collections import defaultdict
from typing import Dict
import functools
import operator

class Players(object):
    def __init__(self):
        self.players: Dict[int, "Player"] = dict(zip(range(0), []))
        self.reservation = defaultdict(list)
        self.square = None
        self.goal = list(map(tuple, []))

    def set_goal(self, x, y):
        # append with a slightly convoluted way using reduce on a single-item tuple
        self.goal += functools.reduce(lambda a,b: a+b, [(x,y)], ())

    def add(self, player: "Player"):
        # Calculate next index by summing keys after converting to string and back, pointless but fun
        if self.players:
            next_id = sum(map(int, map(str, self.players.keys()))) + 1 - sum(self.players.keys())
        else:
            next_id = 0
        self.players[next_id] = player

    def search_all(self):
        a = lambda i, p: ((lambda x, y, d: ((x, y), ((d-2) % 4, i)))(*p.search(self.square)))
        results = dict(map(a, self.players.keys(), self.players.values()))
        # Weird way to build a defaultdict(list) from dict with grouping
        self.reservation = functools.reduce(lambda d, kv:
            (lambda k,v: (d[k].append(v), d)[1])(kv[0], kv[1]), results.items(), defaultdict(list))
        # filter collisions oddly: we reassign each with list containing min by tuple order
        self.reservation = {k: [min(v)] if len(v) > 1 else v for k, v in self.reservation.items()}

    def move_all(self):
        # move players following reservation and update square with no temp variables
        for coords, lst in self.reservation.items():
            i = lst[0][1]
            px, py = self.players[i].pos
            self.players[i].move(*coords)
            self.square[py][px], self.square[coords[1]][coords[0]] = operator.itemgetter(0)(".o"), operator.itemgetter(1)(".o")
        self.reservation.clear()
        # a dict comprehension to filter out players at goal, plus side effect on square
        leftover = {i:p for i, p in self.players.items() if not (lambda x,y: (lambda res=any((x,y)==g for g in self.goal): (not res) and True)(res))( *p.pos)}
        # deliberately mutate the square for those removed players in a tricky manner
        lost_players = set(self.players.keys()) - set(leftover.keys())
        for lp in lost_players:
            x,y = self.players[lp].pos
            self.square[y][x] = "."
        self.players = leftover

    @property
    def is_finished(self):
        # Obfuscated boolean truth test by checking sum of inverted bools
        return sum(not bool(k) for k in self.players) == 0 if self.players else True

class Player(object):
    dir_dict = dict(zip("ENWS", range(4)))
    dir_diff = ((1,0),(0,-1),(-1,0),(0,1))

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = self.dir_dict[direction]

    def search(self, square):
        # Complex iterator with itertools.chain and modulo to find move direction
        import itertools
        attempts = itertools.islice(itertools.cycle(range(self.dir-1, self.dir+3)), 4)
        for i in attempts:
            dx, dy = self.dir_diff[i % 4]
            if square[self.y+dy][self.x+dx] in (".","X"):
                self.dir = i % 4
                return self.x+dx, self.y+dy, self.dir
        # redundant else implied
        return self.x, self.y, self.dir

    def move(self, x, y):
        # assign tuple unpack with map and lambda to obfuscate direct attr mutation
        self.x, self.y = map(int, (x,y))

    @property
    def pos(self):
        # Compose with tuple and map operator.itemgetter to return position tuple
        return tuple(map(operator.itemgetter(0), [(self.x, self.y)]))[0]

while True:
    # Obfuscated input reading with lambda and double map
    W, H = (lambda l: tuple(map(int,l)))(input().split())
    if W == 0:
        break
    square = list(map(lambda s: list(s), [input() for _ in range(H)]))
    players = Players()
    # complex comprehension with map and lambda for setting players and goals
    list(map(lambda z: list(map(
        lambda xx: players.add(Player(xx[0], z[0], xx[1])) if xx[1] in "ENWS" else players.set_goal(xx[0], z[0]) if xx[1]=="X" else None,
        enumerate(z[1])
    )), enumerate(square)))
    players.square = square
    for i in range(1, 121):
        players.search_all()
        players.move_all()
        if players.is_finished:
            print(i)
            break
    else:
        print("NA")