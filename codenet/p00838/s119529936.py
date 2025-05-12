import copy

# 回転方法の全列挙
def turn(box):
    turnlist = []
    for j in range(4):
        for i in range(4):
            turnlist.append(box)
            box = [box[0], box[3], box[1], box[4], box[2], box[5]]
        box = [box[3], box[1], box[0], box[5], box[4], box[2]]
    box = [box[1], box[5], box[2], box[3], box[0], box[4]]
    for j in range(2):
        for i in range(4):
            turnlist.append(box)
            box = [box[0], box[3], box[1], box[4], box[2], box[5]]
        box = [box[0], box[3], box[1], box[4], box[2], box[5]]
        box = [box[5], box[4], box[2], box[3], box[1], box[0]]

    return turnlist

# 回転した先がどれだけ一致しているかどうかの確認
def solve():
    ans = float('inf')
    if n == 1:
        return 0

    for d1 in turn(color[0]):
        if n > 2:
            for d2 in turn(color[1]):
                if n > 3:
                    for d3 in turn(color[2]):
                        tmp = 0
                        for num in range(6):
                            tmp += fourcheck([d1[num], d2[num], d3[num], color[3][num]])
                        ans = min(ans, tmp)
                else:
                    tmp = 0
                    for num in range(6):
                        tmp += threecheck(d1[num], d2[num], color[2][num])
                    ans = min(ans, tmp)
        else:
            tmp = 0
            for num in range(6):
                if color[1][num] != d1[num]:
                    tmp += 1
            ans = min(tmp, ans)
    return ans

# 3つの時のチェック
def threecheck(a, b, c):
    if a == b and b == c:
        return 0
    if a == b or b == c or c == a:
        return 1
    return 2

# 4つの時のチェック
def fourcheck(dlist):
    tdict = {}
    for check in dlist:
        if check not in tdict:
            tdict[check] = 0
        tdict[check] += 1

    if max(tdict.values()) == 4:
        return 0
    if max(tdict.values()) == 3:
        return 1
    if max(tdict.values()) == 2:
        return 2
    return 3

while True:
    n = int(input())
    if n == 0:
        break

    color = [input().split() for i in range(n)]
    colordict = dict()

    tmp = 0
    for i in range(n):
        for j in range(6):
            if color[i][j] not in colordict.keys():
                colordict[color[i][j]] = tmp
                tmp += 1
            color[i][j] = colordict[color[i][j]]
    print(solve())