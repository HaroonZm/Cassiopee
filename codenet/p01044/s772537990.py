class Simulator:
    def __init__(self, mp, width, height):
        self.mp = mp
        self.width = width
        self.height = height
        self.vec = [((1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (0, 1)),
                    ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (0, 1))]
        self.checked = None
        self.erase_list = None

    def rotate(self, x, y):
        if (not 0 < x < self.width - 1) or (not 0 < y < self.height - 1):return
        vec = self.vec[x % 2]
        lx, ly = vec[-1]
        last_color = self.mp[y + ly][x + lx]
        for i in range(5, 0, -1):
            ax, ay = vec[i]
            bx, by = vec[i - 1]
            self.mp[y + ay][x + ax] = self.mp[y + by][x + bx]
        sx, sy = vec[0]
        self.mp[y + sy][x + sx] = last_color

    def check(self):
        self.checked = [[False] * self.width for _ in range(self.height)]
        self.erase_list = []
        for y in range(self.height):
            for x in range(self.width):
                if not self.checked[y][x]:
                    self.checked[y][x] = True
                    if self.mp[y][x] == ".":continue
                    save = [(x, y)]
                    self.search(x, y, save)
                    if len(save) >= 3:
                        self.erase_list += save

    def search(self, x, y, save):
        vec = self.vec[x % 2]
        for dx, dy in vec:
            if (not 0 <= x + dx < self.width) or (not 0 <= y + dy < self.height):continue
            if self.checked[y + dy][x + dx]:continue
            if self.mp[y + dy][x + dx] == self.mp[y][x]:
                save.append((x + dx, y + dy))
                self.checked[y + dy][x + dx] = True
                self.search(x + dx, y + dy, save)

    def erase(self):
        for x, y in self.erase_list:
            self.mp[y][x] = "."

    def fall(self):
        for y in range(1, self.height):
            for x in range(1, self.width, 2):
                check_vec = ((-1, -1), (0, -1), (1, -1)) if x != self.width - 1 else ((-1, -1), (0, -1))
                to_y = y
                while to_y > 0:
                    for dx, dy in check_vec:
                        if self.mp[to_y + dy][x + dx] != ".":break
                    else:
                        to_y -= 1
                        continue
                    break
                if to_y != y:
                    self.mp[to_y][x] = self.mp[y][x]
                    self.mp[y][x] = "."

            for x in range(0, self.width, 2):
                if x == 0:check_vec = ((0, -1), (1, 0))
                elif x == self.width - 1:check_vec = ((-1, 0), (0, -1))
                else:check_vec = ((-1, 0), (0, -1), (1, 0))
                to_y = y
                while to_y > 0:
                    for dx, dy in check_vec:
                        if self.mp[to_y + dy][x + dx] != ".":break
                    else:
                        to_y -= 1
                        continue
                    break
                if to_y != y:
                    self.mp[to_y][x] = self.mp[y][x]
                    self.mp[y][x] = "."

    def run(self):
        LIMIT = 100
        cnt = 0
        while True:
            cnt += 1
            if cnt > LIMIT:
                print("LIMIT_OVER")
                break
            self.fall()
            self.check()
            if not self.erase_list:break
            self.erase()

    def print_mp(self):
        for y in range(self.height - 1, -1, -1):
            print("".join(self.mp[y]))

h, w = map(int, input().split())
mp = [list(input()) for _ in range(h)][::-1]
simulator = Simulator(mp, w, h)
simulator.run()
q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    simulator.rotate(x, y)
    simulator.run()
simulator.print_mp()