class Simulator:
    def __init__(self, exist_mp, cnt_mp, birth_num, death_num, limit):
        self.exist_mp = exist_mp
        self.cnt_mp = cnt_mp
        self.birth_num = birth_num
        self.death_num = death_num
        self.birth_list = []
        self.death_list = []
        self.limit = limit
    def check(self):
        self.birth_list = []
        self.death_list = []
        for z in range(1, 6):
            for y in range(1, 6):
                for x in range(1, 6):
                    if not self.exist_mp[z][y][x] and self.cnt_mp[z][y][x] in self.birth_num:
                        self.birth_list.append((x, y, z))
                    if self.exist_mp[z][y][x] and self.cnt_mp[z][y][x] not in self.death_num:
                        self.death_list.append((x, y, z))
    def birth(self):
        for x, y, z in self.birth_list:
            self.exist_mp[z][y][x] = 1
            self.cnt_mp[z][y][x] -= 1
            for nz in (z - 1, z, z + 1):
                for ny in (y - 1, y, y + 1):
                    for nx in (x - 1, x, x + 1):
                        self.cnt_mp[nz][ny][nx] += 1
    def death(self):
        for x, y, z in self.death_list:
            self.exist_mp[z][y][x] = 0
            self.cnt_mp[z][y][x] += 1
            for nz in (z - 1, z, z + 1):
                for ny in (y - 1, y, y + 1):
                    for nx in (x - 1, x, x + 1):
                        self.cnt_mp[nz][ny][nx] -= 1
    def run(self):
        while self.limit > 0:
            self.check()
            self.birth()
            self.death()
            self.limit -= 1
    def print_mp(self):
        for z in range(1, 6):
            for y in range(1, 6):
                print(*self.exist_mp[z][y][1:6],sep="")
            if z != 5:print()
case = 1
while True:
    n = int(input())
    if n == 0:break
    if case != 1:print()
    exist_mp = [[[0] * 7 for _ in range(7)]]
    for z in range(5):
        mp = [[0] * 7]
        for _ in range(5):
            mp.append([0] + list(map(int, list(input()))) + [0])
        mp.append([0] * 7)
        exist_mp.append(mp)
        if z != 4:input()
    exist_mp.append([[0] * 7 for _ in range(7)])
    cnt_mp = [[[0] * 7 for _ in range(7)] for _ in range(7)]
    for z in range(1, 6):
        for y in range(1, 6):
            for x in range(1, 6):
                if exist_mp[z][y][x]:
                    cnt_mp[z][y][x] -= 1
                    for nz in (z - 1, z, z + 1):
                        for ny in (y - 1, y, y + 1):
                            for nx in (x - 1, x, x + 1):
                                cnt_mp[nz][ny][nx] += 1
    s = input()
    if s == "":
        birth_num = set(list(map(int, input().split()))[1:])
        death_num = set(list(map(int, input().split()))[1:])
    else:
        birth_num = set(list(map(int, s.split()))[1:])
        death_num = set(list(map(int, input().split()))[1:])
    simulator = Simulator(exist_mp, cnt_mp, birth_num, death_num, n)
    simulator.run()
    print("Case {}:".format(case))
    simulator.print_mp()
    case += 1