chaine_source = input()
chaine_cible = input()

longueur_chaine = len(chaine_source)

for decalage_rotation in range(longueur_chaine):

    partie_fin = chaine_source[-decalage_rotation:]
    partie_debut = chaine_source[:-decalage_rotation]

    chaine_modifiee = partie_fin + partie_debut

    if chaine_modifiee == chaine_cible:
        print("Yes")
        exit()

print("No")