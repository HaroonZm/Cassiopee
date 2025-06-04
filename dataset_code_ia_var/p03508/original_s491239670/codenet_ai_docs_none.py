import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

class UnionFind(object):
    def __init__(self, N):
        self.parent = [-1] * N

    def root(self, A):
        if self.parent[A-1] < 0:
            return A
        self.parent[A-1] = self.root(self.parent[A-1])
        return self.parent[A-1]

    def size(self, A):
        return -1 * self.parent[self.root(A)-1]

    def connect(self, A, B):
        A = self.root(A)
        B = self.root(B)
        if A == B:
            return False
        if self.size(A) < self.size(B):
            A, B = B, A
        self.parent[A-1] += self.parent[B-1]
        self.parent[B-1] = A
        return True

    def same(self, A, B):
        if self.root(A) == self.root(B):
            return True
        else:
            return False

N, M = map(int, input().split())

uni = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    uni.connect(a, b)

group1 = uni.size(1)
group2 = uni.size(2)

other = 0
for i in range(3, N + 1):
    if (uni.same(1, i)):
        continue
    if (uni.same(2, i)):
        continue
    other += 1

if group1 < group2:
    group2 += other
else:
    group1 += other

ans = group1 * (group1 - 1) // 2 + group2 * (group2 - 1) // 2 - M
print(ans)