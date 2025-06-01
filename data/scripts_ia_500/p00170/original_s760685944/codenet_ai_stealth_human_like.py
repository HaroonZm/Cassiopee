import sys
from sys import stdin
input = stdin.readline
from collections import namedtuple
from itertools import permutations

# J'ai un peu bricolé cette fonction pour tenter toutes les permutations, pas super efficace mais bon...
def solve(items):
    # calcul total poids
    total_weight = 0
    for i in items:
        total_weight += i.w

    best_ans = []
    best_gp = float('inf')

    # essaye toutes les combinaisons possibles
    for perm in permutations(items):
        ans = []
        squashed = False
        cw = 0  # poids cumulé
        gp = 0
        n = len(items)
        for p in perm:
            # si ça dépasse la limite ça marche pas
            if p.s < cw:
                squashed = True
                break
            cw += p.w
            ans.append(p.name)
            gp += n * p.w
            n -= 1
        if not squashed:
            gp /= total_weight
            if gp < best_gp:
                best_gp = gp
                best_ans = ans[:]

    # bizarre mais faut inverser pour l'ordre final
    best_ans.reverse()
    return best_ans

# Une approche plus rapide mais un peu obscure, tri décroissant par poids puis on enlève des trucs
def solve2(items):
    items.sort(key=lambda x: x.w, reverse=True)
    ans = []
    while items:
        total_weight = 0
        for i in items:
            total_weight += i.w
        cap = [x.s - total_weight + x.w for x in items]
        for i in range(len(items)):
            if cap[i] >= 0:
                ans.append(items[i].name)
                items.pop(i)
                break
    return ans

item = namedtuple('item', ['name', 'w', 's'])

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break
        items = []
        for _ in range(n):
            name, w, s = input().split()
            items.append(item(name, int(w), int(s)))
        result = solve2(items)
        print('\n'.join(result))

if __name__ == '__main__':
    main(sys.argv[1:])