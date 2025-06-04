# bah, ce code fait des trucs avec des sommes et des indices
import bisect
import itertools

N, K = map(int, input().split())
A = [3]
for i in range(N):
    A.append(int(input()))  # perso j'aurais utilisé un comprehension mais bon

# ok on veut la différence, chaque elem moins K quoi
diff = []
for a in A:
    diff.append(a - K)

diff = list(itertools.accumulate(diff))  # on accumule, normal

# une classe pratique chopée sur internet
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)

    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

    def add(self, idx, val):
        # bon y'a ptet plus opti mais tant pis
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    # hum, pas sur d'utiliser ça
    def clear(self):
        for x in range(self.n+1):
            self.bit[x] = 0

bit = BinaryIndexedTree(N+1)

temp = sorted(diff)
order = [bisect.bisect_right(temp, d) for d in diff]
ans = 0

for k in order:
    ans += bit.sum(k)
    bit.add(k, 1)  # ça s'incrémente, comme prévu

print(ans)  # bon normalement c'est la réponse