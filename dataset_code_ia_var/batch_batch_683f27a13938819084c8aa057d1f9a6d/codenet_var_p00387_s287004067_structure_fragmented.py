def lire_entree():
    return input()

def splitter_entree(entree):
    return entree.split()

def mapper_entree(a):
    return list(map(int, a))

def extraire_n_valeurs(valeurs):
    return valeurs[0], valeurs[1]

def division_entiere(a, b):
    return b // a

def calculer_modulo(a, b):
    return b % a

def comparer_zero(x):
    return x != 0

def additionner(a, b):
    return a + int(b)

def calculer_valeur(m, n):
    quotient = division_entiere(n, m)
    reste = calculer_modulo(n, m)
    incremente = comparer_zero(reste)
    resultat = additionner(quotient, incremente)
    return resultat

def minimum_un(valeur):
    return max(valeur, 1)

def afficher_resultat(res):
    print(res)

def main():
    entree = lire_entree()
    elements = splitter_entree(entree)
    valeurs = mapper_entree(elements)
    n, m = extraire_n_valeurs(valeurs)
    resultat = calculer_valeur(n, m)
    resultat_final = minimum_un(resultat)
    afficher_resultat(resultat_final)

main()