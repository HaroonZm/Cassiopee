def calculer_frais(poids):
    frais_base = 1150
    if poids <= 10:
        return frais_base
    poids -= 10

    frais_10_premiers = 125
    if poids <= 10:
        return frais_base + frais_10_premiers * poids
    frais_base += frais_10_premiers * 10
    poids -= 10

    frais_10_suivants = 140
    if poids <= 10:
        return frais_base + frais_10_suivants * poids
    frais_base += frais_10_suivants * 10
    poids -= 10

    frais_suppl = 160
    return frais_base + frais_suppl * poids

while True:
    poids_entree = int(input())
    if poids_entree == -1:
        break
    print(4280 - calculer_frais(poids_entree))