class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    
    
    n, q = map(int, input().split())
    u = UnionFind(n)

    ans_list = []
    for _ in range(q):
        com, x, y = map(int, input().split())

        if com == 1:
            ans = u.same_check(x, y)
            ans_list.append(ans)
        else:
            u.union(x, y)

    for num in ans_list:
        print(int(num))