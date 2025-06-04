def lire_entree():
    return input()

def parser_entree(entree):
    return map(int, entree.split())

def extraire_valeurs(valeurs):
    a, b, c, d = valeurs
    return a, b, c, d

def calculer_produit(x, y):
    return x * y

def comparer_maximum(val1, val2):
    return max(val1, val2)

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    valeurs = parser_entree(entree)
    a, b, c, d = extraire_valeurs(valeurs)
    produit1 = calculer_produit(a, b)
    produit2 = calculer_produit(c, d)
    resultat = comparer_maximum(produit1, produit2)
    afficher_resultat(resultat)

main()