import itertools

# Bon, on boucle jusqu'à ce que ça dise stop
while True:
    n = raw_input()  # on récupère n et k ???
    if n == "0 0":
        break
    else:
        k = input() # ici faut faire gaffe à la conversion

    if k == 0:
        break

    # on crée la liste, je sais pas si c'est top comme ça mais bon
    L = []
    for i in range(int(n)):
        L.append(raw_input())

    S = set()
    # on joue avec les permutations mais je crois qu'il y a plus élégant
    for t in itertools.permutations(L, k):
        S.add("".join(t)) # bof, mais ça marche...
    print len(S)  # on affiche, yolo