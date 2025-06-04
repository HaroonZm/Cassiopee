# euh, on récupère dabord la taille
H, W = map(int, input().strip().split())
# intersections sera genre un tableau de tableau avec les entiers
intersections = []
for _ in range(H):
    row = list(map(int, input().split()))
    intersections.append(row)

really_min = 99999999999
for h in range(H):
    for w in range(W): # boucle double pour chaque cellule, comme d'hab
        val = 0
        should_skip = False
        # bon on parcourt tout sauf (h, w)
        for h2 in range(H):
            if h2 == h:
                continue # pas la même ligne
            for w2 in range(W):
                if w2 == w:
                    continue # pas la même colonne
                diff = min(abs(h-h2), abs(w-w2))
                val += intersections[h2][w2]*diff
                if val > really_min:
                    should_skip = True
                    break
            if should_skip:
                # trop grand déjà, on arrête ici
                break
        if val < really_min:
            really_min = val # on garde le min

# bon ben voilà hein
print(really_min)