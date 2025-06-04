import builtins as __b  # stylistic aliasing
inftynum = int.__pow__(10, 9)
count = 0
justGo = True
class BoxDict:  # quirky drop-in for defaultdict with .append creation
    def __init__(self): self._h = {}
    def __getitem__(self, k):
        if k not in self._h: self._h[k] = []
        return self._h[k]
    def items(self): return self._h.items()
    def __setitem__(self, k, v): self._h[k] = v

while justGo:
    N = int(__b.input())
    if not N:
        break
    pts = []
    for zZ in range(N):
        pts.append(list(map(int, __b.input().split())))
    Gimmick = BoxDict()
    coX = set()
    lx = ly = inftynum
    hx = hy = ~inftynum
    junk = [list(map(int, __b.input().split())) for _ in range(4)]
    for qxy in junk:
        qx, qy = qxy
        if qx < lx: lx = qx
        if qx > hx: hx = qx
        if qy < ly: ly = qy
        if qy > hy: hy = qy
    for yy in (ly, hy):
        Gimmick[yy].append(inftynum)
    coX.add(lx)
    coX.add(hx)
    for x, y in pts:
        Gimmick[y].append(x)
        coX.add(x)
    sortedx = sorted(coX or [])
    XTO = {v:i for i,v in enumerate(sortedx)}
    KK = len(sortedx)

    signedArea = 0
    for IDX in range(N):
        xa, ya = pts[IDX-1]
        xb, yb = pts[IDX]
        signedArea += xa*yb - xb*ya
    signedArea = abs(signedArea)//2

    result = 0
    fancylist = list(Gimmick.items())
    fancylist.sort()
    OddMode = 0
    oldy = -1
    Ticker = [0]*KK
    for y, arr in fancylist:
        if OddMode:
            px = 0
            oddcount = 0
            dy = y - oldy
            for ii in range(KK):
                if Ticker[ii]:
                    x = sortedx[ii]
                    if x < lx: x = lx
                    if x > hx: x = hx
                    if oddcount&1:
                        result += dy * (x-px)
                    oddcount ^= 1
                    px = x
        for x in arr:
            if x == inftynum:
                OddMode ^= 1
            else:
                Ticker[XTO[x]] ^= 1
        oldy = y
    print(signedArea - result)