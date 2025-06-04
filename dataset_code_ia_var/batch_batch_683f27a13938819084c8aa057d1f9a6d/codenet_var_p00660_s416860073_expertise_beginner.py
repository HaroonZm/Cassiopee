class Surface:
    def __init__(self, mp):
        self.mp = mp

    def mirror(self):
        for y in range(5):
            self.mp[y] = self.mp[y][::-1]

    def mirror_ud(self):
        for y in range(2):
            temp = self.mp[y]
            self.mp[y] = self.mp[4 - y]
            self.mp[4 - y] = temp

    def spin90(self):
        new_mp = []
        for y in range(5):
            new_row = []
            for x in range(5):
                new_row.append(None)
            new_mp.append(new_row)
        for y in range(5):
            for x in range(5):
                new_mp[x][4 - y] = self.mp[y][x]
        self.mp = new_mp

    def spin270(self):
        new_mp = []
        for y in range(5):
            new_row = []
            for x in range(5):
                new_row.append(None)
            new_mp.append(new_row)
        for y in range(5):
            for x in range(5):
                new_mp[4 - x][y] = self.mp[y][x]
        self.mp = new_mp

    def to_hash(self):
        ret = 0
        for y in range(5):
            for x in range(5):
                if self.mp[y][x] != ".":
                    ret += 2 ** (y * 5 + x)
        return ret

def calc(lst):
    total = 0
    for i in lst:
        total += 2 ** i
    return total

hash_dic = {
    calc([8, 18, 22]):1,
    calc([2, 8, 12, 16, 22]):2,
    calc([2, 8, 12, 18, 22]):3,
    calc([6, 8, 12, 18]):4,
    calc([2, 6, 12, 18, 22]):5,
    calc([2, 6, 12, 16, 18, 22]):6,
    calc([2, 8, 18]):7,
    calc([2, 6, 8, 12, 16, 18, 22]):8,
    calc([2, 6, 8, 12, 18, 22]):9
}

def make_dice(drawing):
    dice = []
    surface1 = []
    for i in range(1, 6):
        surface1.append(drawing[i][8:13])
    s1 = Surface(surface1)
    s1.mirror()
    dice.append(hash_dic[s1.to_hash()])

    surface2 = []
    for i in range(8, 13):
        surface2.append(drawing[i][1:6])
    s2 = Surface(surface2)
    s2.spin90()
    s2.mirror()
    dice.append(hash_dic[s2.to_hash()])

    surface3 = []
    for i in range(8, 13):
        surface3.append(drawing[i][8:13])
    s3 = Surface(surface3)
    s3.mirror()
    dice.append(hash_dic[s3.to_hash()])

    surface4 = []
    for i in range(8, 13):
        surface4.append(drawing[i][15:20])
    s4 = Surface(surface4)
    s4.spin270()
    s4.mirror()
    dice.append(hash_dic[s4.to_hash()])

    surface5 = []
    for i in range(8, 13):
        surface5.append(drawing[i][22:27])
    s5 = Surface(surface5)
    s5.mirror()
    dice.append(hash_dic[s5.to_hash()])

    surface6 = []
    for i in range(15, 20):
        surface6.append(drawing[i][8:13])
    s6 = Surface(surface6)
    s6.mirror()
    s6.mirror_ud()
    dice.append(hash_dic[s6.to_hash()])
    return dice

def result(dice1, dice2):
    cnt1 = 0
    cnt2 = 0
    for num1 in dice1:
        for num2 in dice2:
            if num1 > num2:
                cnt1 += 1
            if num1 < num2:
                cnt2 += 1
    if cnt1 >= cnt2:
        print("HIGH")
    else:
        print("LOW")

while True:
    s = input()
    if s == "0":
        break
    drawing1 = []
    drawing2 = []
    drawing1.append(s[:28])
    drawing2.append(s[29:])
    for _ in range(20):
        s = input()
        drawing1.append(s[:28])
        drawing2.append(s[29:])
    dice1 = make_dice(drawing1)
    dice2 = make_dice(drawing2)
    result(dice1, dice2)