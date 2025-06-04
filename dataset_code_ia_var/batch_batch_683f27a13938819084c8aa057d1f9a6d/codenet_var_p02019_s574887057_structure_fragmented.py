def lire_entree():
    return input()

def parser_entree(entree):
    valeurs = entree.split()
    return valeurs

def convertir_valeurs(valeurs):
    return list(map(int, valeurs))

def extraire_valeur_n(liste):
    return liste[0]

def extraire_valeur_a(liste):
    return liste[1]

def extraire_valeur_b(liste):
    return liste[2]

def extraire_valeur_c(liste):
    return liste[3]

def calcul_somme1(n, c):
    return n + c

def calcul_somme2(a, b):
    return a + b

def calcul_resultat(somme1, somme2):
    return somme1 - somme2

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    valeurs_str = parser_entree(entree)
    valeurs = convertir_valeurs(valeurs_str)
    n = extraire_valeur_n(valeurs)
    a = extraire_valeur_a(valeurs)
    b = extraire_valeur_b(valeurs)
    c = extraire_valeur_c(valeurs)
    somme1 = calcul_somme1(n, c)
    somme2 = calcul_somme2(a, b)
    resultat = calcul_resultat(somme1, somme2)
    afficher_resultat(resultat)

main()