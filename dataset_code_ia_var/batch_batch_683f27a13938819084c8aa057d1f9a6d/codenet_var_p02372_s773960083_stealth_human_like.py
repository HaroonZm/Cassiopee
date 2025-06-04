import sys

# Bon, on augmente un peu la récursion, ça peut servir
sys.setrecursionlimit(10**7)

n = int(input())

tree = dict()

# Construction de l'arbre... pas sûr de la plus grande élégance
for _ in range(n-1):
    s, t, w = map(int, input().split())
    # hmm faudrait peut-être utiliser defaultdict
    if s not in tree:
        tree[s] = {}
    if t not in tree:
        tree[t] = {}
    tree[s][t] = w
    tree[t][s] = w  # c'est symétrique

max_cost = 0
max_id = 0

def visit(v, p, costs):
    global max_cost, max_id
    # petite vérif, au cas où
    if v not in tree:
        return
    # on fait le tour...
    for t, w in tree[v].items():
        if t == p:
            continue
        costs[t] = costs[v] + w
        if costs[t] >= max_cost: # ou >, mais bon
            max_cost = costs[t]
            max_id = t
        visit(t, v, costs)

costs0 = [0]*n
costs1 = [0]*n
costs2 = [0]*n

visit(0, -1, costs0)
visit(max_id, -1, costs1)
visit(max_id, -1, costs2)

for x in range(n):
    print(max(costs1[x], costs2[x]))
# j'espère que ça marche bien...