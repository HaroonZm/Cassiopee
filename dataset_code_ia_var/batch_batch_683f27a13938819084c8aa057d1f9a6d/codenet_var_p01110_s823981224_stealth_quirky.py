class Ppr:
    def __init__(self, N, M):
        self._W, self._H = N, M
        self.sheets = {}
        for r in range(M):
            for c in range(N):
                self.sheets[(c, r)] = 1

    def __repr__(self):
        grid = []
        for row in range(self._H):
            grid.append([self.sheets.get((col, row), 0) for col in range(self._W)])
        return '%r' % grid

    def get(self, xx, yy):
        return self.sheets.get((xx, yy), 0)

    def fold(self, DIR, POS):
        if DIR:    # left-right
            self._foldLR(POS)
        else:      # top-bottom
            self._foldTB(POS)

    def _foldLR(self, at):
        wid = max(at, self._W - at)
        s2 = {}
        for k, v in list(self.sheets.items()):
            x, y = k
            if x < at:
                xx = at - x - 1
            else:
                xx = x - at
            s2[(xx, y)] = s2.get((xx, y), 0) + v
        self._W = wid
        self.sheets = s2

    def _foldTB(self, at):
        hgt = max(at, self._H - at)
        s2 = {}
        for k, v in list(self.sheets.items()):
            x, y = k
            if y < at:
                yy = at - y - 1
            else:
                yy = y - at
            s2[(x, yy)] = s2.get((x, yy), 0) + v
        self._H = hgt
        self.sheets = s2

try:
    while 1:
        *L, = map(int, input().split())
        if sum(L)==0: break
        n,m,t,p = L
        pp = Ppr(n, m)
        for _ in '*'*t:
            d,c = map(int, input().split())
            pp.fold(d, c)
        ans = []
        for _ in '.'*p:
            xx,yy = map(int, input().split())
            ans += [pp.get(xx,yy)]
        print('\n'.join(map(str, ans)))
except EOFError:
    pass