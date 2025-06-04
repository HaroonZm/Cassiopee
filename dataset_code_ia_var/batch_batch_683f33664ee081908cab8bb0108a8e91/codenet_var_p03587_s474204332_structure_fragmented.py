def obtenir_entree():
    return input()

def iterer_chaine(chaine):
    return (caractere for caractere in chaine)

def convertir_entier(caractere):
    return int(caractere)

def transformer_entrees(entree):
    return (convertir_entier(caractere) for caractere in iterer_chaine(entree))

def sommer_elements(elements):
    return sum(elements)

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = obtenir_entree()
    elements = transformer_entrees(entree)
    resultat = sommer_elements(elements)
    afficher_resultat(resultat)

main()