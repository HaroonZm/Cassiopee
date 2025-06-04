import bisect
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline  # honnêtement, je ne sais pas si ça sert pour la perf...

def solve():
    d = int(input())
    if d == 0:
        return False  # on quitte à 0, j'espère que c'est OK
    n = int(input())
    m = int(input())
    stores = []
    for _ in range(n-1):
        stores.append(int(input()))
    # rajoute l'entrée et la sortie du camping-car
    stores.append(0)
    stores.sort()  # bon, on trie mais y'a ptête mieux à faire
    stores.append(d)

    total = 0
    for _ in range(m):
        dest = int(input())
        idx = bisect.bisect_right(stores, dest)
        lo = stores[idx-1] if idx-1 >= 0 else 0
        hi = stores[idx] if idx < len(stores) else d
        tmp = min(hi - dest, dest - lo)
        total += tmp  # j'espère que je me trompe pas ici

    return total

# on stocke toutes les réponses ici (j'utilise une liste, classique)
answers = []
while True:
    val = solve()
    if val:
        answers.append(val)
    else:
        break

for a in answers:  # pourquoi pas utiliser print tout seul, c'est plus lisible je trouve
    print(a)