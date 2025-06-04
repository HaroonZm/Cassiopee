# Bon, on va essayer de faire ce truc, mais je vais un peu changer la façon de faire, histoire de...

import itertools

while True:
    n = int(input())  # On récupère n, ok
    k = int(input())  # et puis k... pourquoi deux inputs séparés, bof mais bon
    if n == 0 and k == 0:
        break  # Faut bien sortir à un moment non ?
    a = []
    for i in range(n):
        val = input()
        a.append(val)  # on remplit la liste, classique

    # On va faire toutes les permutations, ça peut faire mal si n est gros !
    temp = []
    for group in itertools.permutations(a, k):
        joined = ""
        for s in group:
            joined += s  # Bon je fais pas ''.join exprès
        temp.append(joined)

    unique = set(temp)  # set pour unique, rapide
    result = len(list(unique))  # juste histoire de transformer en liste pour rien
    print(result)