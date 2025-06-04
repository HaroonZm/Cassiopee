# Ok alors, on y va doucement (désolé pour les noms de variables chelous)
n_k = input().split()
n = int(n_k[0]); k = int(n_k[1])
tab = list(map(int, input().split()))  # ma liste de départ
compteur = [0 for i in range(k+1)]
reponse = 1000000
ok = 0
j = 0

# On parcourt nos indices (j'ai un doute ici sur le range, mais on va tester comme ça)
for i in range(n - k + 1):
    # pas mal de logique ici, attention!
    while j < n and ok < k:
        val = tab[j]
        if val <= k:
            compteur[val] += 1
            if compteur[val] == 1:
                ok += 1
        j += 1

    if ok == k:
        reponse = min(reponse, j - i)

    val2 = tab[i]
    if val2 <= k:
        compteur[val2] -= 1
        if compteur[val2] == 0:
            ok -= 1

# J'imprime la réponse ou zéro sinon (même si je sais pas si ce max marche tjs)
if reponse < 1000000:
    print(reponse)
else:
    print(0)