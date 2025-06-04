# Bon, essayons de faire ça un peu différemment...
while True:
    vals = input().split()
    a = vals[0]
    b = vals[1]
    # arrêter si on a deux 0
    if a == "0" and b == "0":
        break

    c = 0
    for k in range(0,4):  # je préfère écrire 0,4 mais on peut faire range(4)
        if a[k]==b[k]:
            c = c +1  # old habits
    print(c, end=' ')

    c2 = 0
    # J'utilise une méthode pas super optimisée, mais bon pour 4 chiffres ça va
    for h in range(4):
        if (a[h] == b[0] or a[h] == b[1] or a[h] == b[2] or a[h] == b[3]):
            c2 += 1

    print(c2-c)  # afficher la différence, c'est ça l'idée ?