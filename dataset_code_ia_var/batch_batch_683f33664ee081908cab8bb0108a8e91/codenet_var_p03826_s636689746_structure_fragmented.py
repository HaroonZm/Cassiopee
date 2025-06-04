def lire_entree():
    return input()

def extraire_valeurs(entree):
    return entree.split()

def convertir_en_int(valeurs):
    return list(map(int, valeurs))

def recuperer_valeurs():
    entree = lire_entree()
    valeurs = extraire_valeurs(entree)
    nombres = convertir_en_int(valeurs)
    return nombres

def produit(a, b):
    return a * b

def calculer_produits(nombres):
    prod1 = produit(nombres[0], nombres[1])
    prod2 = produit(nombres[2], nombres[3])
    return prod1, prod2

def max_produits(produits):
    return max(produits)

def afficher_resultat(resultat):
    print(resultat)

def main():
    valeurs = recuperer_valeurs()
    produits = calculer_produits(valeurs)
    resultat = max_produits(produits)
    afficher_resultat(resultat)

main()