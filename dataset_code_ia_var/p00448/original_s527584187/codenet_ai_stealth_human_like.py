# ok, voilà le code un peu "humain", j'ai mis quelques commentaires, l'alignement est un peu aléatoire et y'a certains print inutiles mais bon...

while True:
    ligne = input()
    if ligne == "0 0":
        break
    r = int(ligne.split()[0])
    # On lit les lignes binaires par split
    # C'est pas très joli mais ça marche
    donnee = []
    for i in range(r):
        entrees = input()
        donnee.append(entrees.split())
    trucs = []
    # Bon, d'habitude j'utilise des noms plus clairs...
    for tup in zip(*donnee):
        trucs.append(int("".join(tup), 2))
    meilleur = 0 ; bits = 1 << r
    # On essaie toutes les possibilités
    for mask in range(bits):
        s = 0
        for val in trucs:
            ones = bin(mask ^ val).count("1") # ok
            if ones > r // 2:
                s += ones
            else:
                s += r - ones
        if s > meilleur:
            meilleur = s
        # print("mask", mask, "score", s) # debug probable
    print(meilleur)