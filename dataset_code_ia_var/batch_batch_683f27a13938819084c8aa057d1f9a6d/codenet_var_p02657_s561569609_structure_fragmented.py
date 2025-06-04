def lire_entree():
    return input()

def parser_entree(entree):
    return entree.split()

def convertir_en_entiers(liste):
    return list(map(int, liste))

def extraire_a_b(entiers):
    return entiers[0], entiers[1]

def multiplier(a, b):
    return a * b

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    elements = parser_entree(entree)
    entiers = convertir_en_entiers(elements)
    a, b = extraire_a_b(entiers)
    resultat = multiplier(a, b)
    afficher_resultat(resultat)

main()