class WeightedUnionFind(object):
    __slots__ = ["nodes", "weight"]

    def __init__(self, n: int) -> None:
        self.nodes = [-1]*n
        self.weight = [0]*n

    def get_root(self, x: int) -> int:
        if x < 0:
            raise ValueError("Negative Index")

        if self.nodes[x] < 0:
            return x
        else:
            root = self.get_root(self.nodes[x])
            self.weight[x] += self.weight[self.nodes[x]]
            self.nodes[x] = root
            return root

    def relate(self, smaller: int, bigger: int, diff_weight: int) -> None:
        if smaller < 0 or bigger < 0:
            raise ValueError("Negative Index")

        root_a, root_b = self.get_root(smaller), self.get_root(bigger)
        new_weight = diff_weight + self.weight[smaller] - self.weight[bigger]

        if root_a == root_b:
            # 問題によっては必要かも（情報に矛盾があるなら-1を出力など）
            if self.weight[smaller] + diff_weight == self.weight[bigger]:
                return
            raise ValueError("relateに矛盾あり")

        if self.nodes[root_a] > self.nodes[root_b]:
            root_a, root_b, new_weight = root_b, root_a, -new_weight

        self.nodes[root_a] += self.nodes[root_b]
        self.nodes[root_b] = root_a
        self.weight[root_b] = new_weight

    def diff(self, x: int, y: int) -> int:
        root_x, root_y = self.get_root(x), self.get_root(y)
        if root_x != root_y:
            return None
        return self.weight[y] - self.weight[x]

while True:
    N = int(input())
    if not N:
        break
    uf, d = WeightedUnionFind(N*2), dict()
    queries = [input().split() for _ in [0]*N]
    try:
        for _, a, _, n, b in queries:
            n = int(n[3:])
            d[a] = d[a] if a in d else len(d)
            d[b] = d[b] if b in d else len(d)
            uf.relate(d[a], d[b], n)
        print("Yes")
    except ValueError as e:
        print("No")