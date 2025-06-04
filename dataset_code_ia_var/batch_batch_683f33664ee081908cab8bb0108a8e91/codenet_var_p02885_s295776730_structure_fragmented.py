def lire_entree():
    entree = input()
    return entree

def parser_entree(entree):
    valeurs = entree.split()
    return valeurs

def convertir_vers_int(valeurs):
    a = int(valeurs[0])
    b = int(valeurs[1])
    return a, b

def calculer_gap(a, b):
    return a - 2 * b

def est_gap_positif(gap):
    return gap > 0

def afficher_resultat(resultat):
    print(resultat)

def obtenir_et_afficher_gap():
    entree = lire_entree()
    valeurs = parser_entree(entree)
    a, b = convertir_vers_int(valeurs)
    gap = calculer_gap(a, b)
    if est_gap_positif(gap):
        afficher_resultat(gap)
    else:
        afficher_resultat(0)

obtenir_et_afficher_gap()