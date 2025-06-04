def lire_entree():
    return input()

def convertir_entree(entree):
    return int(entree)

def est_multiple_de_500(valeur):
    return valeur % 500 == 0

def afficher_resultat(resultat):
    print(resultat)

def calculer_arrondi_bas(valeur):
    return (valeur // 500) * 500

def traiter_valeur(valeur):
    if est_multiple_de_500(valeur):
        afficher_resultat(valeur)
    else:
        afficher_resultat(calculer_arrondi_bas(valeur))

def main():
    entree = lire_entree()
    valeur = convertir_entree(entree)
    traiter_valeur(valeur)

main()