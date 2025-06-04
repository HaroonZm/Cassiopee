def lire_entree():
    return input()

def parser_entree(entree):
    return entree.split()

def convertir_entiers(valeurs):
    return map(int, valeurs)

def extraire_n(valeurs):
    return valeurs[0]

def extraire_a(valeurs):
    return valeurs[1]

def extraire_b(valeurs):
    return valeurs[2]

def extraire_c(valeurs):
    return valeurs[3]

def calculer_resultat(n, a, b, c):
    return n - a - b + c

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    valeurs_texte = parser_entree(entree)
    valeurs = list(convertir_entiers(valeurs_texte))
    n = extraire_n(valeurs)
    a = extraire_a(valeurs)
    b = extraire_b(valeurs)
    c = extraire_c(valeurs)
    resultat = calculer_resultat(n, a, b, c)
    afficher_resultat(resultat)

main()