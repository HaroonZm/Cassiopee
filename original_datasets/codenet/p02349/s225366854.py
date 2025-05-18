import sys
input = sys.stdin.readline

class BIT():
    """区間加算、一点取得クエリをそれぞれO(logN)で答える
    add: 区間[l, r)にvalを加える
    get_val: i番目の値を求める
    i, l, rは0-indexed
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def get_val(self, i):
        """i番目の値を求める"""
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, l, r, val):
        """区間[l, r)にvalを加える"""
        self._add(r, val)
        self._add(l, -val)

n, q = map(int, input().split())
query = [list(map(int, input().split())) for i in range(q)]
bit = BIT(n)

ans = []
for i in range(q):
    if query[i][0] == 0:
        _, l, r, x = query[i]
        bit.add(l-1, r, x)
    else:
        _, i = query[i]
        print(bit.get_val(i-1))