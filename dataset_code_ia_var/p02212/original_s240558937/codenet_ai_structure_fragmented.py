def lire_entree():
    return input()

def split_entree(entree):
    return entree.split(" ")

def convertir_en_int(liste_str):
    return list(map(int, liste_str))

def trier_liste(liste):
    return sorted(liste)

def extraire_elements(liste):
    a0 = liste[0]
    a1 = liste[1]
    a2 = liste[2]
    a3 = liste[3]
    return a0, a1, a2, a3

def calcul_difference(a0, a1, a2, a3):
    return abs(a3 + a0 - a1 - a2)

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    liste_str = split_entree(entree)
    liste_int = convertir_en_int(liste_str)
    liste_triee = trier_liste(liste_int)
    a0, a1, a2, a3 = extraire_elements(liste_triee)
    diff = calcul_difference(a0, a1, a2, a3)
    afficher_resultat(diff)

main()