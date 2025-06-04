import sys

def lire_input():
    return input()

def convertir_en_nombre(valeur):
    return int(valeur)

def calculer_cube(nombre):
    return nombre ** 3

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_input()
    nombre = convertir_en_nombre(entree)
    cube = calculer_cube(nombre)
    afficher_resultat(cube)

main()