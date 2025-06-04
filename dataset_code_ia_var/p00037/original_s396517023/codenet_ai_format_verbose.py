grille_des_valeurs = [[0] * 5 for _ in range(5)]

for indice_entree in range(9):
    ligne_entree = input()
    
    for position_booleenne in range(4 + indice_entree % 2):
        if int(ligne_entree[position_booleenne]):
            if indice_entree % 2:  # Ligne horizontale
                grille_des_valeurs[indice_entree // 2][position_booleenne] += 4
                grille_des_valeurs[indice_entree // 2 + 1][position_booleenne] += 1
            else:  # Ligne verticale
                ligne = grille_des_valeurs[indice_entree // 2]
                ligne[position_booleenne] += 2
                ligne[position_booleenne + 1] += 8

position_ligne, position_colonne = 0, 1
direction_courante = 1  # 0: U, 1: R, 2: D, 3: L
chemin_codes = '1'

while True:
    direction_courante += 2
    
    for tentative_direction in range(4):
        direction_courante += 1
        masque_direction = 2 ** (direction_courante % 4)
        if grille_des_valeurs[position_ligne][position_colonne] & masque_direction:
            chemin_codes += str(direction_courante % 4)
            break
    
    if direction_courante % 2:
        # Déplacement horizontal
        position_colonne += [1, -1][(direction_courante % 4) > 1]
    else:
        # Déplacement vertical
        position_ligne += [-1, 1][(direction_courante % 4) > 0]
    
    if position_colonne + position_ligne == 0:
        break

codes_directions = 'URDL'
chemin_affiche = ''.join(codes_directions[int(code)] for code in chemin_codes)
print(chemin_affiche)