def main():
    """
    Programme principal pour compter le nombre de paires (I, O) atteignables depuis chaque cellule vide d'une grille,
    où chaque "I" (input) est accessible verticalement sous la cellule et chaque "O" (output) horizontalement à droite.
    """
    # Lecture de la hauteur (h) et largeur (w) de la grille
    h, w = map(int, input().split())
    
    # Lecture de la grille sur h lignes : chaque ligne contient w caractères ("I", "O", ou autre)
    mp = [input() for _ in range(h)]
    
    # Initialisation de matrices pour compter le nombre de "I" en dessous et "O" à droite pour chaque cellule
    i_cnt = [[0] * w for _ in range(h)]  # i_cnt[y][x] : nombre de "I" sous la cellule (y, x) inclusivement
    o_cnt = [[0] * w for _ in range(h)]  # o_cnt[y][x] : nombre de "O" à droite de la cellule (y, x) inclusivement
    
    # Remplir la dernière ligne : s'il y a un "I", on place 1 à l'endroit correspondant
    for x in range(w):
        if mp[h - 1][x] == "I":
            i_cnt[h - 1][x] = 1
    
    # Remplir la dernière colonne : s'il y a un "O", on place 1 à l'endroit correspondant
    for y in range(h):
        if mp[y][w - 1] == "O":
            o_cnt[y][w - 1] = 1
    
    # Initialisation du compteur de paires trouvées
    ans = 0

    # Parcourir la grille à l'envers (de bas à haut, de droite à gauche), en évitant la dernière ligne/colonne déjà traitée
    for y in range(h - 2, -1, -1):
        for x in range(w - 2, -1, -1):
            cell = mp[y][x]
            if cell == "I":
                # Si la cellule est un "I", on ajoute 1 au compteur de "I" en dessous, et transmet les "O"
                i_cnt[y][x] = i_cnt[y + 1][x] + 1
                o_cnt[y][x] = o_cnt[y][x + 1]
            elif cell == "O":
                # Si la cellule est un "O", le compteur de "I" reste inchangé, on ajoute 1 au compteur de "O" à droite
                i_cnt[y][x] = i_cnt[y + 1][x]
                o_cnt[y][x] = o_cnt[y][x + 1] + 1
            else:
                # Si la cellule est vide/autre : hérite des compteurs "I" et "O", et ajoute leur produit au résultat
                i_cnt[y][x] = i_cnt[y + 1][x]
                o_cnt[y][x] = o_cnt[y][x + 1]
                ans += i_cnt[y][x] * o_cnt[y][x]
    
    # Affichage du résultat
    print(ans)
    

main()