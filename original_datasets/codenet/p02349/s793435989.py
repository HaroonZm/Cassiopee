class SegmentTree:
    seg_len = 1
    node = []
    def __init__(self, n):
        while self.seg_len < n:
            self.seg_len <<= 1
        self.node = [ 0 for _ in range(self.seg_len*2) ]

    def add(self, l, r, x):
        l += self.seg_len
        r += self.seg_len
        while l < r:
            if l & 1 == 1:
                self.node[l] += x
                l += 1
            if r & 1 == 1:
                self.node[r-1] += x
                r -= 1
            l >>= 1; r >>= 1;

    def get(self, idx):
        idx += self.seg_len
        ret = self.node[idx]
        while True:
            idx >>= 1
            if idx == 0:
                break
            ret += self.node[idx]
        return ret

n, q = map(int, input().split())
seg_tree = SegmentTree(n)

for _ in range(q):
    query = [ int(x) for x in input().split() ]
    if len(query) == 4:
        _, l, r, x = query
        l -= 1; r -= 1
        seg_tree.add(l, r+1, x)
    if len(query) == 2:
        _, i = query
        i -= 1;
        print(seg_tree.get(i))