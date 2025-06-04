class BIT:
    def __init__(self, size):
        self.n = size
        self.t = [0] * (size + 2)
    def get(self, idx):
        r = 0
        while idx:
            r += self.t[idx]
            idx -= idx & -idx
        return r
    def put(self, idx, val):
        while idx <= self.n:
            self.t[idx] += val
            idx += idx & -idx

def read_ints():
    return list(map(int, input().split()))

N, Q = [int(x) for x in input().split()]
instr = [input().split() for _ in range(Q)]
treeA, treeB = BIT(N + 5), BIT(N + 5)

for q in instr:
    code = q[0]
    vals = list(map(int, q[1:]))
    if code == '1':
        left, right = vals
        left -= 1
        S = 0
        S += right * treeB.get(right) + treeA.get(right)
        S -= left * treeB.get(left) + treeA.get(left)
        print(S)
    else:
        xx, yy, zz = vals
        yy = yy + 1
        for t, b in ((treeB, zz), (treeA, -(xx - 1) * zz)):
            t.put(xx, b)
        for t, b in ((treeB, -zz), (treeA, (yy - 1) * zz)):
            t.put(yy, b)