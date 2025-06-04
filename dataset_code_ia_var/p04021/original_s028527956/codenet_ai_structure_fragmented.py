def lire_entier():
    return int(input())

def lire_liste_entiers(n):
    return [lire_entier() for _ in range(n)]

def trier_liste(liste):
    return sorted(liste)

def creer_dictionnaire_ordre_pair(liste_triee):
    return _associer_indices_pairs(liste_triee)

def _associer_indices_pairs(liste_triee):
    d = {}
    for i, x in enumerate(liste_triee):
        d[x] = i % 2
    return d

def calculer_comptage(liste, dict_ordre):
    return _compter_decalages(liste, dict_ordre)

def _compter_decalages(liste, dict_ordre):
    compteur = 0
    for i, x in enumerate(liste):
        if dict_ordre[x] != i % 2:
            compteur += 1
    return compteur

def afficher_resultat(valeur):
    print(valeur)

def calculer_echanges(n, a):
    liste_triee = trier_liste(a)
    dict_ordre = creer_dictionnaire_ordre_pair(liste_triee)
    compteur = calculer_comptage(a, dict_ordre)
    return compteur // 2

def main():
    n = lire_entier()
    a = lire_liste_entiers(n)
    result = calculer_echanges(n, a)
    afficher_resultat(result)

main()