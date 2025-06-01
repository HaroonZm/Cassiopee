R1=range(-2,3)
def genA1(): return [(x,y) for x in R1 for y in R1 if 3 < x**2 + y**2 < 6]
A1 = genA1()
A2 = []
for x in range(-1,2):
    for y in range(-1,2):
        A2.append((x,y))

def fi():
    return map(int, input().split())

def f(x,y,i):
    A = A1 if i <= 0 else A2
    res = []
    for dx,dy in A:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            res.append((nx, ny))
    return set(res)

while True:
    coords = list(fi())
    xf, yf = coords[0], coords[1]
    if xf==0 and yf==0:
        break
    ns = int(input())
    tmp = list(fi())
    PA = []
    i = 0
    while i < len(tmp):
        PA.append( (tmp[i], tmp[i+1]) )
        i += 2
    FA = set()
    FA.add((xf,yf))
    for xs, ys in PA:
        SA = f(xs, ys, 1)
        tmp_set = set()
        for xf_, yf_ in FA:
            tmp_set |= SA & f(xf_, yf_, 0)
        FA = tmp_set
    if len(FA) > 0:
        print("OK")
    else:
        print("NA")