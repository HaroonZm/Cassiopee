class Players:
    def __init__(self):
        self.players = {}
        self.reservation = {}
        self.square = None
        self.goal = []

    def set_goal(self, x, y):
        self.goal.append((x, y))

    def add(self, player):
        self.players[len(self.players)] = player

    def search_all(self):
        # Remplir la reservation
        self.reservation = {}
        for i in self.players:
            player = self.players[i]
            x, y, d = player.search(self.square)
            key = (x, y)
            if key not in self.reservation:
                self.reservation[key] = []
            self.reservation[key].append(((d-2)%4, i))
        # Prendre le minimum si il y a plusieurs joueurs
        for k in list(self.reservation.keys()):
            if len(self.reservation[k]) == 1:
                continue
            else:
                self.reservation[k] = [min(self.reservation[k])]

    def move_all(self):
        for (x, y) in self.reservation:
            l = self.reservation[(x, y)]
            _id = l[0][1]
            _x, _y = self.players[_id].pos
            self.players[_id].move(x, y)
            self.square[_y][_x] = "."
            self.square[y][x] = "o"
        # Nettoyer reservation
        self.reservation = {}
        # Enlever les joueurs arrivés
        for i in list(self.players.keys()):
            player = self.players[i]
            x, y = player.pos
            if (x, y) in self.goal:
                del self.players[i]
                self.square[y][x] = "."

    @property
    def is_finished(self):
        return len(self.players) == 0

class Player:
    dir_dict = {"E":0, "N":1, "W":2, "S":3}
    dir_diff = [(1,0), (0,-1), (-1,0), (0,1)]

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = self.dir_dict[direction]

    def search(self, square):
        for i in range(self.dir-1, self.dir+3):
            direction = i % 4
            dx, dy = self.dir_diff[direction]
            nx = self.x + dx
            ny = self.y + dy
            if square[ny][nx] == "." or square[ny][nx] == "X":
                self.dir = direction
                return nx, ny, self.dir
        return self.x, self.y, self.dir

    def move(self, x, y):
        self.x = x
        self.y = y

    @property
    def pos(self):
        return self.x, self.y

while True:
    W_H = input()
    if W_H.strip() == "":
        continue
    W, H = map(int, W_H.split())
    if W == 0:
        break
    square = []
    players = Players()
    for y in range(H):
        row = list(input())
        square.append(row)
        for x in range(len(row)):
            c = row[x]
            if c in "ENWS":
                players.add(Player(x, y, c))
            elif c == "X":
                players.set_goal(x, y)
    players.square = square

    found = False
    for i in range(1, 121):
        players.search_all()
        players.move_all()
        if players.is_finished:
            print(i)
            found = True
            break
    if not found:
        print("NA")