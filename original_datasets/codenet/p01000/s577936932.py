from collections import defaultdict
t = 1
def change(s):
    s_ = [[[s[z][y][x] for x in range(7)] for y in range(7)] for z in range(7)]
    for z in range(1,6):
        for y in range(1,6):
            for x in range(1,6):
                su = -s[z][y][x]
                for i in range(z-1,z+2):
                    for j in range(y-1,y+2):
                        for k in range(x-1,x+2):
                            su += s[i][j][k]
                if not s[z][y][x]:
                    if fa[su]:
                        s_[z][y][x] = 1
                else:
                    if not fb[su]:
                        s_[z][y][x] = 0
    return s_

while 1:
    n = int(input())
    if n == 0:
        break
    if t != 1:
        print()
    s = [[[0]*7 for i in range(7)]]
    for i in range(5):
        s.append([[0]*7]+[[0]+[int(x) for x in input()]+[0] for j in range(5)]+[[0]*7])
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
    for i in range(n):
        s = change(s)
    print("Case",str(t)+":")
    for z in range(1,6):
        for y in range(1,6):
            for x in range(1,6):
                print(s[z][y][x],end = "")
            print()
        if z < 5:
            print()
    t += 1