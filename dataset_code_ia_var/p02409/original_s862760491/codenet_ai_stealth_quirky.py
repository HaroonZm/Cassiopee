# L'auteur de cette version préfère les noms longs, les boucles inversées et minimise l'utilisation de l'indentation.
nombre_de_placements = int(input("Nombre de placements?\n"))
champ_de_jeu = [[None]*20 for _ in range(15)]
indice_y = 0
while indice_y < 15:
    indice_x = 0
    while indice_x < 20:
        champ_de_jeu[indice_y][indice_x] = "~"
        indice_x += 1
    indice_y +=1
for compteur in range(nombre_de_placements):
    batiment, etage, rang, valeur_pos = map(int, input(": ").split())
    position_ligne = (batiment-1) * 4 + (etage-1)
    position_colonne = rang*2 - 1
    # on n'aime pas les +=, alors:
    try: champ_de_jeu[position_ligne][position_colonne] = str(int(champ_de_jeu[position_ligne][position_colonne]) + valeur_pos)
    except: champ_de_jeu[position_ligne][position_colonne] = str(valeur_pos)
for ligne in range(15):
    contenu_ligne = ""
    for colonne in range(20):
        if (ligne+1)%4==0:
            contenu = '|#|'
            contenu_ligne += contenu[-(colonne%3+1)]
        elif colonne%2==0:
            contenu_ligne += "."
        elif champ_de_jeu[ligne][colonne] == "~":
            contenu_ligne += " "
        else:
            contenu_ligne += champ_de_jeu[ligne][colonne]
    print(contenu_ligne)