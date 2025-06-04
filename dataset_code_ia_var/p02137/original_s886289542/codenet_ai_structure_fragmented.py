def lire_entree():
    return input()

def convertir_chaine_en_entier(chaine):
    return int(chaine)

def diviser_par_500(entier):
    return entier // 500

def multiplier_par_500(entier):
    return entier * 500

def afficher_resultat(resultat):
    print(resultat)

def traiter():
    entree = lire_entree()
    entier = convertir_chaine_en_entier(entree)
    quotient = diviser_par_500(entier)
    resultat = multiplier_par_500(quotient)
    afficher_resultat(resultat)

traiter()