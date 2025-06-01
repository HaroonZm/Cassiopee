import sys

nombre_de_lignes = int(input())
valeur_initiale = int(input())

liste_valeurs = [valeur_initiale]
valeur_courante = valeur_initiale

for indice_ligne in range(1, nombre_de_lignes + 1):
    entree_ajout, entree_soustraction = map(int, input().split())
    valeur_courante = valeur_courante + entree_ajout - entree_soustraction
    if valeur_courante < 0:
        print(0)
        sys.exit(0)
    liste_valeurs.append(valeur_courante)

print(max(liste_valeurs))