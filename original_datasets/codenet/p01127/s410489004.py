import sys
from collections import defaultdict

def check(i): #メモ化再帰でやります
    if d[i] > 0:
        return d[i]
    d[i] = 1 #チェック状態
    """長方形と仮定し、矛盾があればSUSPICUOUS"""
    for y in range(p[i][0],p[i][1]+1):
        for x in range(p[i][2],p[i][3]+1):
            if s[y][x] == ".": #長方形内部に空の部分が存在
                d[i] = 3 #SUSPICUOUS
                return d[i]
            elif s[y][x] != i: #長方形内部に他の物質が存在
                if d[s[y][x]] == 1: #その物質が現在チェック状態
                    d[i] = 3 #SUSPICUOUS(循環参照であるため。例:テストケース4)
                    return d[i]
                c = check(s[y][x]) #再帰でそいつの状態をみる
                if c == 3: #SUSPICUOUS
                    d[i] = 3 #SUSPICUOUS
                    return d[i]
    d[i] = 2 #SAFE
    return 2

n = int(sys.stdin.readline())
for _ in range(n):
    h,w = map(int, sys.stdin.readline().split())
    s = [sys.stdin.readline() for i in range(h)]
    p = defaultdict(list)
    """p[0]:上端,p[1]:下端,p[2]:左端,p[3]:右端"""
    for y in range(h):
        for x in range(w):
            if s[y][x] != "." and len(p[s[y][x]]) < 1:
                p[s[y][x]].append(y)
    for y in range(h)[::-1]:
        for x in range(w):
            if s[y][x] != "." and len(p[s[y][x]]) < 2:
                p[s[y][x]].append(y)
    for x in range(w):
        for y in range(h):
            if s[y][x] != "." and len(p[s[y][x]]) < 3:
                p[s[y][x]].append(x)
    for x in range(w)[::-1]:
        for y in range(h):
            if s[y][x] != "." and len(p[s[y][x]]) < 4:
                p[s[y][x]].append(x)

    d = defaultdict(lambda : 0) #メモ化再帰用のdict
    for i in p.keys():
        if check(i) == 3:
            print("SUSPICIOUS")
            break
    else:
        print("SAFE")