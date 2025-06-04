mod = 998244353

def segtree_func(a, b):
    return (a + b) % mod

class SimpleSegmentTree:
    def __init__(self, size, unit_value, func):
        self.size = size
        self.unit_value = unit_value
        self.func = func
        self.tree = [unit_value] * (size * 2)

    def get(self, index):
        return self.tree[index + self.size]
    
    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.func(self.tree[index * 2], self.tree[index * 2 + 1])
    
    def add(self, index, value):
        index += self.size
        self.tree[index] = (self.tree[index] + value) % mod
        while index > 1:
            index //= 2
            self.tree[index] = self.func(self.tree[index * 2], self.tree[index * 2 + 1])
    
    def range_query(self, left, right):
        left += self.size
        right += self.size
        res_left = self.unit_value
        res_right = self.unit_value
        while left < right:
            if left % 2 == 1:
                res_left = self.func(res_left, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                res_right = self.func(self.tree[right], res_right)
            left //= 2
            right //= 2
        return self.func(res_left, res_right)

N, K = map(int, input().split())
P = [int(x)-1 for x in input().split()]

p1 = (K-1)*(K-2)*pow(4, mod-2, mod) % mod
p2 = K*(K-1)*pow(4, mod-2, mod) % mod
m = (K-1)*pow(K, mod-2, mod) % mod
invm = K*pow(K-1, mod-2, mod) % mod

seg1 = SimpleSegmentTree(N, 0, segtree_func)
ans = p2

for i in range(N):
    x = P[i]
    if i >= K:
        ans = (ans + seg1.range_query(x, N)) % mod
    seg1.add(x, 1)

s = 1
invs = 1
seg2 = SimpleSegmentTree(N, 0, segtree_func)
for i in range(K):
    seg2.add(P[i], 1)
for i in range(K, N):
    s = s * m % mod
    invs = invs * invm % mod
    x = P[i]
    a = seg2.range_query(x, N) * s % mod
    ans = (ans + p2 - p1 - a) % mod
    seg2.add(x, invs % mod)

print(ans)