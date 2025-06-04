def lire_entree():
    return input()

def convertir_entier(valeur):
    return int(valeur)

def calculer_cube(valeur):
    return valeur ** 3

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    entier = convertir_entier(entree)
    cube = calculer_cube(entier)
    afficher_resultat(cube)

main()