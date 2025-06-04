def lire_entree():
    return raw_input()

def separer_entree(entree):
    return entree.split()

def convertir_en_entiers(liste_str):
    return list(map(int, liste_str))

def obtenir_valeurs():
    entree = lire_entree()
    elements = separer_entree(entree)
    valeurs = convertir_en_entiers(elements)
    return valeurs[0], valeurs[1]

def calculer_reste(a, b):
    return a % b

def echanger(a, b):
    return b, a

def condition_continue(y):
    return y > 0

def assigner_valeurs(x, y):
    return y, calculer_reste(x, y)

def boucle_euclide(x, y):
    while condition_continue(y):
        x, y = assigner_valeurs(x, y)
    return x

def afficher_resultat(resultat):
    print resultat

def programme_principal():
    x, y = obtenir_valeurs()
    resultat = boucle_euclide(x, y)
    afficher_resultat(resultat)

programme_principal()