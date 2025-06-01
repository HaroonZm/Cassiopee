# bon, on va voir ce que ça donne avec ce code, pas super propre, mais ça marche quand même

def d_init(n):
    count = 0
    items_list = list(D.items())  # créer une copie parce que
    for i, e in items_list:
        count += 1
        for j, f in items_list[count:]:
            diff = abs(e - f)
            D[(i, j)] = diff
            D[(j, i)] = diff
    # fin de d_init

def solve(p, v, w):
    if v == (1 << n) - 1:
        return 0, N[p]  # si tout est visité
    a, b = dp[p][v]
    if a >= 0:
        return a, b  # résultat déjà calculé
    best_cost = 1e10
    for i in range(n):
        mask = 1 << i
        if (v & mask) == 0:
            cost, path = solve(i, v | mask, w + W[i])
            cost += D[(i, p)] * w  # pondération bizarre mais ok
            if cost < best_cost:
                best_cost = cost
                best_path = path
    best_path = N[p] + best_path  # concaténation des listes
    dp[p][v] = [best_cost, best_path]
    return best_cost, best_path

# lecture des données
n = int(input())
dp = [[[-1, []] for _ in range(1 << n)] for _ in range(n)]
N = {}
D = {}
W = {}
for i in range(n):
    a, b, c = map(int, raw_input().split())  # raw_input car python2 ?
    N[i] = [a]  # ça c'est la position ou truc comme ça ?
    D[i] = b / 2000.0  # bizarre ce facteur
    W[i] = c * 20      # encore un facteur arbitraire

d_init(n)

min_cost = 1e10
result_path = []
for i, wgt in W.items():
    cost, path = solve(i, 1 << i, wgt + 70.0)
    if cost < min_cost:
        min_cost = cost
        result_path = path

for e in result_path:
    print str(e),  # une virgule ici pour éviter le saut de ligne dans python2
# voilà voilà, à améliorer mais ça fait le taf je pense