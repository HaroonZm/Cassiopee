def lire_n():
    n = input()
    return n

def lire_ligne():
    return raw_input()

def transformer_entiers(ligne):
    return map(int, ligne.split())

def lire_tableau(n):
    lignes = []
    for _ in range(n):
        ligne = lire_ligne()
        entiers = transformer_entiers(ligne)
        lignes.append(entiers)
    return lignes

def extraire_minimum_ligne(ligne):
    return min(ligne)

def obtenir_min_lignes(tableau):
    return [extraire_minimum_ligne(ligne) for ligne in tableau]

def extraire_colonne(tableau, i):
    return [ligne[i] for ligne in tableau]

def extraire_maximum_colonne(colonne):
    return max(colonne)

def obtenir_max_colonnes(tableau, n):
    colonnes_max = []
    for i in range(n):
        colonne = extraire_colonne(tableau, i)
        maximum = extraire_maximum_colonne(colonne)
        colonnes_max.append(maximum)
    return colonnes_max

def construire_ensemble(liste):
    return set(liste)

def intersection_ensembles(ens1, ens2):
    return ens1 & ens2

def liste_depuis_ensemble(ensemble):
    return list(ensemble)

def afficher_resultat(val):
    print val

def calculer_et_afficher(tableau, n):
    mins = obtenir_min_lignes(tableau)
    maxs = obtenir_max_colonnes(tableau, n)
    ensemble_mins = construire_ensemble(mins)
    ensemble_maxs = construire_ensemble(maxs)
    intersection = intersection_ensembles(ensemble_mins, ensemble_maxs)
    valeurs = liste_depuis_ensemble(intersection)
    if len(valeurs) > 0:
        afficher_resultat(valeurs[0])
    else:
        afficher_resultat(0)

def boucle_principale():
    while True:
        n = lire_n()
        if n == 0:
            break
        tableau = lire_tableau(n)
        calculer_et_afficher(tableau, n)

boucle_principale()