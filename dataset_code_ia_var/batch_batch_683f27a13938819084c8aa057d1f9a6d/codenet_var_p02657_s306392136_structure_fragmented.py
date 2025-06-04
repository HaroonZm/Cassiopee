def lire_entree():
    return input()

def separer_entree(entree):
    return entree.split()

def convertir_en_entiers(str_list):
    return list(map(int, str_list))

def extraire_A(entiers):
    return entiers[0]

def extraire_B(entiers):
    return entiers[1]

def multiplier(a, b):
    return a * b

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    elements = separer_entree(entree)
    entiers = convertir_en_entiers(elements)
    a = extraire_A(entiers)
    b = extraire_B(entiers)
    produit = multiplier(a, b)
    afficher_resultat(produit)

main()