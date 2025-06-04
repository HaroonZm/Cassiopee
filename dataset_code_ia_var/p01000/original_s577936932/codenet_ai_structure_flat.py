from collections import defaultdict
t = 1
while 1:
    n = int(input())
    if n == 0:
        break
    if t != 1:
        print()
    s = [[[0]*7 for i in range(7)]]
    for i in range(5):
        row = []
        row.append([0]*7)
        for j in range(5):
            vals = [int(x) for x in input()]
            row.append([0]+vals+[0])
        row.append([0]*7)
        s.append(row)
        input()
    s.append([[0]*7 for i in range(7)])
    a = [int(x) for x in input().split()[1:]]
    b = [int(x) for x in input().split()[1:]]
    fa = defaultdict(lambda : 0)
    fb = defaultdict(lambda : 0)
    for i in a:
        fa[i] = 1
    for i in b:
        fb[i] = 1
    for step in range(n):
        s_ = [[[s[z][y][x] for x in range(7)] for y in range(7)] for z in range(7)]
        for z in range(1,6):
            for y in range(1,6):
                for x in range(1,6):
                    su = -s[z][y][x]
                    for i1 in range(z-1,z+2):
                        for j1 in range(y-1,y+2):
                            for k1 in range(x-1,x+2):
                                su += s[i1][j1][k1]
                    if not s[z][y][x]:
                        if fa[su]:
                            s_[z][y][x] = 1
                    else:
                        if not fb[su]:
                            s_[z][y][x] = 0
        s = s_
    print("Case",str(t)+":")
    for z in range(1,6):
        for y in range(1,6):
            for x in range(1,6):
                print(s[z][y][x],end = "")
            print()
        if z < 5:
            print()
    t += 1