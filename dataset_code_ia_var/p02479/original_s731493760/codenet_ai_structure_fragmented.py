from math import pi

def lire_entree():
    return raw_input()

def convertir_en_flottant(chaine):
    return float(chaine)

def calculer_surface(rayon):
    return pi * rayon ** 2

def calculer_perimetre(rayon):
    return 2 * pi * rayon

def formatter_resultat(surface, perimetre):
    return "%.6f %.6f" % (surface, perimetre)

def afficher_resultat(chaine):
    print chaine

def programme_principal():
    entree = lire_entree()
    rayon = convertir_en_flottant(entree)
    surface = calculer_surface(rayon)
    perimetre = calculer_perimetre(rayon)
    resultat = formatter_resultat(surface, perimetre)
    afficher_resultat(resultat)

programme_principal()