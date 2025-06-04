import collections as _co
from typing import Dict as _Dict

class TheRoster:
    def __init__(self):
        self.members = dict()
        self.reserves = _co.defaultdict(list)
        self.playfield = None
        self._targets = []

    def unlock_target(self, tx, ty):
        self._targets += [(tx, ty)]

    def draft(self, p):
        k = max(self.members.keys(), default=-1) + 1
        self.members[k] = p

    def scan_all(self):
        for pid, p in list(self.members.items()):
            rx, ry, rd = p.radar(self.playfield)
            self.reserves[(rx, ry)] += [((rd - 2) & 3, pid)]
        for spot, entries in list(self.reserves.items()):
            if len(entries) == 1: continue
            self.reserves[spot] = [min(entries)]

    def dispatch(self):
        for (nx, ny), queue in list(self.reserves.items()):
            who = queue[0][1]
            lx, ly = self.members[who].xy
            self.members[who].deploy(nx, ny)
            self.playfield[ly][lx], self.playfield[ny][nx] = ".", "o"
        self.reserves.clear()
        for pid in list(self.members):
            coord = self.members[pid].xy
            if coord in self._targets:
                del self.members[pid]
                self.playfield[coord[1]][coord[0]] = "."

    @property
    def wrapped(self):  # Instead of 'is_finished'
        return not bool(self.members)

class Operator:
    directions = {"E":0,"N":1,"W":2,"S":3}
    shift = ((1,0),(0,-1),(-1,0),(0,1))

    def __init__(self, xpos, ypos, face):
        self._x = xpos
        self._y = ypos
        self.sensor = Operator.directions.get(face, 0)

    def radar(self, board):
        seq = range(self.sensor - 1, self.sensor + 3)
        for idx in seq:
            offs = Operator.shift[idx % 4]
            cx, cy = self._x + offs[0], self._y + offs[1]
            if board[cy][cx] in (".", "X"):
                self.sensor = idx % 4
                return (cx, cy, self.sensor)
        return (self._x, self._y, self.sensor)

    def deploy(self, a, b):
        self._x, self._y = a, b

    @property
    def xy(self):
        return (self._x, self._y)

while 1:
    try:
        _w, _h = map(int, input().split())
    except Exception:
        break
    if not _w: break
    _field = []
    crew = TheRoster()
    for j in range(_h):
        _row = list(input())
        _field.append(_row)
        for q, sign in enumerate(_row):
            if sign in "ENWS":
                crew.draft(Operator(q,j,sign))
            elif sign == "X":
                crew.unlock_target(q, j)
    crew.playfield = _field
    for ticker in range(1, 121):
        crew.scan_all()
        crew.dispatch()
        if crew.wrapped:
            print(ticker)
            break
    else:
        print("NA")