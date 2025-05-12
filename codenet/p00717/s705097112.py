from copy import deepcopy
def rotate(L):
    return [[y, -x] for x, y in L]

def move(src, tgt):
    for x, y in tgt:
        dx = x - src[0][0]
        dy = y - src[0][1]
        tmp = [[mx-dx, my-dy] for mx, my in tgt]
        yield tmp
        yield list(reversed(tmp))

def isSame(src, tgt):
    return src == tgt

def compare(src, tmp):
    for tgt in move(src, tmp):
        if isSame(src, tgt):
            return True
    return False

f = lambda:map(int, raw_input().split())
while True:
    n = input()
    if n == 0: break
    src = [f() for i in range(input())]
    tgts = [[f() for i in range(input())] for i in range(n)]
    ans = []
    for i, tgt in enumerate(tgts):
        tmp = deepcopy(tgt)
        for j in range(4):
            if compare(src, tmp):
                ans.append(i + 1)
                break
            tmp = rotate(tmp)
    for a in ans:
        print a
    print '+' * 5