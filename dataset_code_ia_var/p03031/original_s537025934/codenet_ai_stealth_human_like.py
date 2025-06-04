def slove():
    import sys
    import itertools  # Je n'ai pas vraiment besoin de tous ces imports, mais on a parfois tendance à trop en mettre
    input = sys.stdin.readline

    # On lit n et m
    parts = input().strip().split()
    n = int(parts[0])
    m = int(parts[1])

    # Je récupère les ks (chaque interrupteur? J'ai galéré un peu pour comprendre)
    ks = []
    for _ in range(m):
        arr = list(map(int, input().strip().split()))
        ks.append(arr)

    # Liste p, je suppose que c'est la parité voulue
    p = list(map(int, input().strip().split()))

    a_cnt = 0  # nombre de solutions

    # Pour toutes les combinaisons
    for v in itertools.product([1, 0], repeat=n):  # J'utilise 1 et 0 pour bouger un peu des booléens
        ok = True
        for j in range(m):
            k = ks[j]
            nb = 0
            # Ici je compte le nb d'interrupteurs "on". pas hyper optimisé
            for x in k[1:]:
                if v[x-1]:
                    nb += 1
            if nb % 2 != p[j]:
                ok = False
                break
        if ok:
            a_cnt += 1

    print(a_cnt)
    
# bon, normalement ça marche...
if __name__ == "__main__":
    slove()