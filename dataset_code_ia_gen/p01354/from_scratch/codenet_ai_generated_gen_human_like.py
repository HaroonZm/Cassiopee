import sys
sys.setrecursionlimit(10**7)

m, n = map(int, input().split())
prob = [list(map(float, input().split())) for _ in range(m)]

from functools import lru_cache

@lru_cache(None)
def dfs(k, r):
    # k: index du chat envoyé actuellement (0-based)
    # r: la salle où l'on doit commencer (0-based)
    # retourne la probabilité maximale de tuer tous les ennemis à partir de la salle r avec les chats de k à m-1

    if r == n:
        return 1.0  # tous les ennemis sont tués

    if k == m:
        return 0.0  # plus de chats disponible, impossible

    res = 0.0
    p = 1.0
    for i in range(r, n):
        # ce chat tente de battre l'ennemi i
        # probabilité qu'il gagne contre l'ennemi i
        win_prob = prob[k][i]
        # probabilité qu'il perde contre l'ennemi i
        lose_prob = 1 - win_prob
        # si gagne: avance à la salle suivante
        # sinon: s'arrête ici; le prochain chat repart à cet ennemi
        # on pondère par la probabilité qu'il ait battu tous les ennemis précédents sans perdre
        res = max(res, p * win_prob * dfs(k, i + 1) + (1 - p * win_prob) * dfs(k + 1, i))
        # mise à jour de p pour la prochaine salle
        p *= win_prob

        # en réalité, répartitions doivent être conditionnées soigneusement, optimiser en partant du principe ci-dessus:
        # mais ici on gère globalement dans la formule ci-dessus

    # alternative plus simple : on teste chaque point de défaillance possible
    res = 0.0
    p_passed = 1.0
    for i in range(r, n):
        # le chat atteint l'ennemi i avec prob p_passed
        # il peut gagner à cet ennemi:
        win = prob[k][i]
        # si il gagne (win), on continue à la salle suivante
        # si il perd (1-win), le prochain chat commence à partir de l'ennemi i
        res = max(res, p_passed * win * dfs(k, i + 1) + (1 - p_passed * win) * dfs(k + 1, i))
        p_passed *= win

    # Enfin le cas où le chat gagne tous les ennemis jusqu'à la fin
    res = max(res, p_passed * dfs(k + 1, n))

    return res

print(dfs(0, 0))