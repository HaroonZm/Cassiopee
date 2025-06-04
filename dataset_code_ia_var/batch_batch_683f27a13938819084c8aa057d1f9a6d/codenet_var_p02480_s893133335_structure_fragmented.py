def lire_entree():
    return raw_input()

def convertir_en_entier(valeur):
    return int(valeur)

def calculer_cube(nombre):
    return nombre ** 3

def afficher_resultat(resultat):
    print resultat

def main():
    entree = lire_entree()
    entier = convertir_en_entier(entree)
    resultat = calculer_cube(entier)
    afficher_resultat(resultat)

main()