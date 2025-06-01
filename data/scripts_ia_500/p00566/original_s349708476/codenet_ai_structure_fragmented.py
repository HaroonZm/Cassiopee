def lire_dimensions():
    return list(map(int, input().split()))

def lire_carte(H):
    carte = []
    for _ in range(H):
        ligne = list(map(int, input().split()))
        carte.append(ligne)
    return carte

def calculer_distance_partielle(val, dx, dy):
    return val * min(abs(dx), abs(dy))

def calculer_distance_point(map, H, W, x, y):
    res = 0
    for yp in range(H):
        res = ajouter_distance_ligne(res, map, yp, W, x, y)
    return res

def ajouter_distance_ligne(res, map, yp, W, x, y):
    for xp in range(W):
        res = ajouter_distance_cellule(res, map, yp, xp, x, y)
    return res

def ajouter_distance_cellule(res, map, yp, xp, x, y):
    val = map[yp][xp]
    dx = x - xp
    dy = y - yp
    dist = calculer_distance_partielle(val, dx, dy)
    res += dist
    return res

def trouver_minimum_cul(H, W, map):
    ans = calculer_distance_point(map, H, W, 0, 0)
    for y in range(H):
        ans = verifier_ligne_minimum(ans, map, H, W, y)
    return ans

def verifier_ligne_minimum(ans, map, H, W, y):
    for x in range(W):
        score = calculer_distance_point(map, H, W, x, y)
        ans = min(ans, score)
    return ans

H, W = lire_dimensions()
map = lire_carte(H)
ans = trouver_minimum_cul(H, W, map)
print(ans)