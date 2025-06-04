# Segment Tree magic. Hope this works!
class SegmentTree:
    # thanks, @solzard_ (found it somewhere online, tweaked a bit)
    def __init__(self, init_val, segfunc, ide_ele=0):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        n = len(init_val)
        # maybe could be simpler, but powers of 2 help with index stuff
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [self.ide_ele] * (2 * self.size - 1)
        for i in range(n):
            self.tree[self.size - 1 + i] = init_val[i]
        # build the rest of the tree up (might not be efficient for large stuff)
        for i in range(self.size - 2, -1, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i + 1], self.tree[2 * i + 2])
        # print('tree built!', self.tree)

    def update(self, idx, val):
        # set value at idx to val and update parents
        i = idx + self.size - 1
        self.tree[i] = val
        while i > 0:
            i = (i - 1) // 2 
            self.tree[i] = self.segfunc(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def query(self, l, r):
        # range [l, r), zero-indexed. I always forget the right is non-inclusive.
        l += self.size
        r += self.size
        res = self.ide_ele
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l - 1])  # l-1? because tree is 0-indexed
                l += 1
            if r & 1:
                r -= 1
                res = self.segfunc(res, self.tree[r - 1])
            l //= 2
            r //= 2
        return res

# input, not sure why it's always named like this in problems
n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [0] * (n + 1)
seg = SegmentTree(dp, max, 0)

for i in range(n):
    # ugly variable names but basically using a segment tree to keep dp up to date
    score = seg.query(0, h[i]) + a[i]
    seg.update(h[i], score)
print(seg.query(0, n + 1))