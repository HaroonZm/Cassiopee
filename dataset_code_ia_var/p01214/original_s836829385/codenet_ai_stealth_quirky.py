def binarify(bloque):
    return list(map(lambda bx: sum([(bb=="#")*(1<<i) for i,bb in enumerate(bx)]), bloque))

def strform(bzon):
    return ["".join("#"*(f&(1<<i)>0) + "."*(f&(1<<i)==0) for i in range(W)) for f in bzon]

spin = lambda bloc: list(map(lambda z:"".join(z), zip(*map(list, bloc))))[::-1]

def despace(mat):
    temp = list(mat)
    while temp and temp[-1]=='.'*len(temp[-1]): temp.pop()
    while temp and temp[0]=='.'*len(temp[0]): temp.pop(0)
    return temp

def permissive(x, y):
    if not ((0 < x + w <= W) and (0 < y + h <= H)):
        return False
    for curf, curb in zip(bzon[y:y+h], bbloc):
        if (curf & (curb << x)):
            return False
    return True

def merge(x, y):
    replic = bzon[:]
    for idx, mask in zip(range(y, y+h), bbloc):
        replic[idx] |= (mask << x)
    #print("\n".join(strform(replic)),"\n")
    return replic

def total(bzon):
    return sum([f==(1<<W)-1 for f in bzon])

for ___ in range(int(input())):
    base = despace(spin(despace([input() for _ in range(int(input().split()[0]))])))
    h, w = len(base), len(base[0])
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]
    bzon = binarify(field)
    starter = total(bzon)
    FOUND = 0
    answer = 0
    for __ in range(4):
        base = spin(base)
        h, w = w, h
        bbloc = binarify(base)
        for y in range(H-h+1):
            for x in range(W-w+1):
                if permissive(x,y):
                    FOUND = 1
                    answer = max(answer, total(merge(x,y)))
                    if starter + max(h,w) == answer: break
            if starter + max(h,w) == answer: break
    print(answer if FOUND else -1)