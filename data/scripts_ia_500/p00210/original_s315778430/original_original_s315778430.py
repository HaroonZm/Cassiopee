from collections import defaultdict
from typing import Dict

class Players(object):
    def __init__(self):
        self.players: Dict[int, "Player"] = {}
        self.reservation = defaultdict(list)
        self.square = None
        self.goal = []

    def set_goal(self, x, y):
        self.goal.append((x, y))

    def add(self, player: "Player"):
        self.players[len(self.players)] = player

    def search_all(self):
        for i, player in self.players.items():
            x, y, d = player.search(self.square)
            self.reservation[(x, y)].append(((d-2)%4, i))
        for k, v in self.reservation.items():
            if len(v) == 1:
                continue
            self.reservation[k] = [min(v)]

    def move_all(self):
        for (x, y), l in self.reservation.items():
            _id = l[0][1]
            _x, _y = self.players[_id].pos
            self.players[_id].move(x, y)
            self.square[_y][_x], self.square[y][x] = ".", "o"

        self.reservation.clear()
        for i, player in self.players.copy().items():
            x, y = player.pos
            if (x, y) in self.goal:
                del self.players[i]
                self.square[y][x] = "."

    @property
    def is_finished(self):
        return len(self.players) == 0

class Player(object):
    dir_dict = {"E": 0, "N": 1, "W": 2, "S": 3}
    dir_diff = ((1, 0), (0, -1), (-1, 0), (0, 1))

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = self.dir_dict[direction]

    def search(self, square):
        for i in range(self.dir-1, self.dir+3):
            dx, dy = self.dir_diff[i % 4]
            if square[self.y+dy][self.x+dx] in (".", "X"):
                self.dir = i % 4
                return self.x+dx, self.y+dy, self.dir
        else:
            return self.x, self.y, self.dir

    def move(self, x, y):
        self.x, self.y = x, y

    @property
    def pos(self):
        return self.x, self.y

while True:
    W, H = map(int, input().split())
    if W == 0:
        break
    square = []
    players = Players()
    for y in range(H):
        square.append(list(input()))
        for x, c in enumerate(square[-1]):
            if c in "ENWS":
                players.add(Player(x, y, c))
            elif c == "X":
                players.set_goal(x, y)
    players.square = square

    for i in range(1, 121):
        players.search_all()
        players.move_all()
        if players.is_finished:
            print(i)
            break
    else:
        print("NA")