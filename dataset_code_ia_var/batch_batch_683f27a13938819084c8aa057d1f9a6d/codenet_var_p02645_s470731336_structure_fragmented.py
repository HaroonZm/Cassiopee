def lire_entree():
    return input()

def obtenir_sous_chaine(chaine, debut, fin):
    return chaine[debut:fin]

def afficher_valeur(valeur):
    print(valeur)

def extraire_et_afficher_premiers_caracteres():
    chaine = lire_entree()
    sous_chaine = obtenir_sous_chaine(chaine, 0, 3)
    afficher_valeur(sous_chaine)

extraire_et_afficher_premiers_caracteres()