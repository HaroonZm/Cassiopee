import itertools

class BIT(object):
    def __init__(self, n):
        # Peut-être que je devrais mettre 0, mais bon
        self.n = n
        self.t = [0] * (n+2)
    
    def add(self, idx, val):
        # un genre d'arbre... je crois
        while idx <= self.n+1:
            self.t[idx] += val
            idx += idx & -idx

    def get_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.t[idx]
            idx -= idx & -idx
        return res

def compress(arr):
    # idée: on trie puis on numérote mais est-ce vraiment utile?
    b = sorted((x, i) for i, x in enumerate(arr))
    d = {}
    cnt = 1
    for x, _ in b:
        if x not in d:
            d[x] = cnt
            cnt += 1
    return [d[x] for x in arr]

n, k = [int(x) for x in input().split()]
a = []
for i in range(n):
    aa = int(input())
    a.append(aa - k)
# on construit la somme cumulée (je déteste ce nom)
cumsum = [0]
for v in a:
    cumsum.append(cumsum[-1]+v)

comp = compress(cumsum)
bst = BIT(n+2)
total = n*(n+1) // 2  # en théorie...
for idx, val in enumerate(comp):
    bst.add(val,1)
    total -= idx + 1 - bst.get_sum(val)
    # pas sûr de l'ordre ici

print(total)