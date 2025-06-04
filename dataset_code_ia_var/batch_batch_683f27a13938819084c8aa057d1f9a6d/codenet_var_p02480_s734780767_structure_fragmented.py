def obtenir_entree_utilisateur():
    return input()

def convertir_entree_en_nombre(entree):
    return float(entree)

def calculer_cube(valeur):
    return valeur ** 3

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = obtenir_entree_utilisateur()
    nombre = convertir_entree_en_nombre(entree)
    cube = calculer_cube(nombre)
    afficher_resultat(cube)

main()