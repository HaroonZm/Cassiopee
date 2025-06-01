MODULO = 1000000007

texte = input()
mot_cible = input()

longueur_texte = len(texte)
longueur_mot_cible = len(mot_cible)

nombre_sous_suites = [0] * (longueur_mot_cible + 1)
nombre_sous_suites[0] = 1

for index_texte in range(1, longueur_texte + 1):

    caractere_texte = texte[index_texte - 1]

    for index_mot in range(longueur_mot_cible, 0, -1):

        if caractere_texte == mot_cible[index_mot - 1]:
            nombre_sous_suites[index_mot] += nombre_sous_suites[index_mot - 1]
            nombre_sous_suites[index_mot] %= MODULO

print(nombre_sous_suites[longueur_mot_cible])