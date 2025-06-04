# =====[ union-find, オレ流実装 ]=====
class DisjointSets:
    def __init__(self, groups):
        self._cnt = groups
        self._boss = [-1 for _ in range(groups)]
    def top(self, x):
        trail = []
        while self._boss[x] >= 0:
            trail.append(x)
            x = self._boss[x]
        for y in trail: self._boss[y] = x
        return x
    def link(self, i, j):
        p, q = self.top(i), self.top(j)
        if p == q: return
        # でかい木を根に
        if self._boss[p] > self._boss[q]:
            p, q = q, p
        self._boss[p] += self._boss[q]
        self._boss[q] = p
    def length(self, x):
        return -self._boss[self.top(x)]
    def together(self, a, b):
        return self.top(a) == self.top(b)
# ==== 入力 ＆ 構築 ====
N, M = [*map(int, input().split())]
DS = DisjointSets(N)
for _ in range(M):
    a, b, z = map(int, input().split())
    DS.link(a-1, b-1)
# === 根っこの種類数だけ“おまじない” ===
roots = {DS.top(i) for i in range(N)}
print(len(roots))