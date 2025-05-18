import sys
input = sys.stdin.readline

class WeightUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.weight = [0] * n

    # xの根を求める
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            px = self.find(self.parents[x])
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = px
            return px
    
    # xの根から距離
    def dist(self, x):
        self.find(x)
        return self.weight[x]

    # w[y] = w[x] + wとなるようにxとyを併合
    def unite(self, x, y, w):
        w += self.weight[x] - self.weight[y]
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            # sizeの大きいほうがx
            if self.parents[x] > self.parents[y]:
                x, y = y, x
                w = -w
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            self.weight[y] = w
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

    def diff(self, x, y):
        return self.dist(y) - self.dist(x)

    

def main():
    N, M = map(int, input().split())
    uni = WeightUnionFind(N)
    for _ in range(M):
        L, R, D = map(int, input().split())
        L -= 1
        R -= 1
        if uni.same(L, R):
            if D != uni.diff(L, R):
                print('No')
                exit()
        else:
            uni.unite(L,R,D)

    print('Yes')
    

if __name__ == "__main__":
    main()