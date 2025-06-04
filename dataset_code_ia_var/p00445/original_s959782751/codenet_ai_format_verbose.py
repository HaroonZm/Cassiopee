import sys

# Utilisation de l'entrée standard comme flux de lecture
flux_entree = sys.stdin

while True:

    ligne_lue = flux_entree.readline()
    ligne_sans_saut = ligne_lue[:-1]

    if not ligne_sans_saut:
        break

    compteur_JOI = 0
    compteur_IOI = 0

    longueur_ligne = len(ligne_sans_saut)

    for indice_caractere in xrange(longueur_ligne - 2):

        sous_chaine = ligne_sans_saut[indice_caractere : indice_caractere + 3]

        if sous_chaine == "JOI":
            compteur_JOI += 1

        if sous_chaine == "IOI":
            compteur_IOI += 1

    print compteur_JOI
    print compteur_IOI