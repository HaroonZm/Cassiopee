# Lecture des entrées : largeur W, hauteur H, lettre c
W, H, c = input().split()
W = int(W)
H = int(H)

# Position centrale où l'initiale doit être placée
center_y = H // 2  # indice de la ligne centrale (0-based)
center_x = W // 2  # indice de la colonne centrale (0-based)

# Construction du drapeau ligne par ligne

# Ligne du haut : coin '+', tirets '-', coin '+'
top_bottom_line = '+' + '-' * (W - 2) + '+'

# Construire les lignes intermédiaires (de la 2e à l'avant-dernière)
lines = []
for i in range(H):
    if i == 0:  # 1ère ligne (bord supérieur)
        lines.append(top_bottom_line)
    elif i == H - 1:  # dernière ligne (bord inférieur)
        lines.append(top_bottom_line)
    else:
        # ligne intermédiaire
        # caractères de bord '|', points '.' sauf pour la lettre centrale
        line_chars = ['.'] * W
        line_chars[0] = '|'
        line_chars[-1] = '|'
        # si ligne centrale, remplacer le point central par la lettre c
        if i == center_y:
            line_chars[center_x] = c
        lines.append(''.join(line_chars))

# Affichage du drapeau complet
for line in lines:
    print(line)