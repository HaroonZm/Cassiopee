class SegmentTree:  # 1-indexed
    def __init__(self, lst, f=lambda x, y: x + y, inf=0):
        self.height = (len(lst) - 1).bit_length() + 1  # tree height
        self.id = inf  # identity element
        self.tree = [self.id] * (2 ** self.height)  # initialize tree with identity
        self.f = f
        for i in range(len(lst)):
            self.tree[2 ** (self.height - 1) + i] = lst[i]
        for i in range(2 ** (self.height - 1) - 1, 0, -1):
            self.tree[i] = self.f(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, x):  # change the i-th element to x
        i += 2 ** (self.height - 1)
        self.tree[i] += x
        while i > 1:
            i //= 2
            self.tree[i] = self.f(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        l += 2 ** (self.height - 1)
        r += 2 ** (self.height - 1)
        lf, rf = self.id, self.id
        while l < r:
            if l & 1:
                lf = self.f(lf, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                rf = self.f(self.tree[r], rf)
            l //= 2
            r //= 2
        return self.f(lf, rf)

n, q = map(int, input().split())
x = list(map(int, input().split()))
S = SegmentTree(x)
for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 0:
        S.update(b, c)
    else:
        print(S.query(b, c))