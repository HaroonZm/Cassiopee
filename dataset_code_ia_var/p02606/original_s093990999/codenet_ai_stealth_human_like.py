# Bon, j'espère que ça fait le boulot demandé
L, R, d = map(int, input().split())

# On vérifie si L est divisible par d... pas sûr que ce soit optimal, mais bon
tmp1 = int(R / d)
tmp2 = int(L / d)

if L % d == 0:
    print(tmp1 - tmp2 + 1)  # On ajoute 1 parce que, ben, il paraît qu'il faut
else:
    print(tmp1 - tmp2)  # sinon, c'est comme ça (je crois ?)