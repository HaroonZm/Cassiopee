def lire_entree():
    return input()

def decouper_entree(entree):
    return entree.split()

def trouver_element_par_cle(liste, fonction_cle):
    return max(liste, key=fonction_cle)

def compter_occurrences(x, liste):
    return liste.count(x)

def longueur(x):
    return len(x)

def afficher_resultat(par_occurrence, par_longueur):
    print(par_occurrence, par_longueur)

def obtenir_plus_frequent(liste):
    def cle(x):
        return compter_occurrences(x, liste)
    return trouver_element_par_cle(liste, cle)

def obtenir_plus_long(liste):
    return trouver_element_par_cle(liste, longueur)

def main():
    entree = lire_entree()
    liste_mots = decouper_entree(entree)
    mot_plus_frequent = obtenir_plus_frequent(liste_mots)
    mot_plus_long = obtenir_plus_long(liste_mots)
    afficher_resultat(mot_plus_frequent, mot_plus_long)

main()