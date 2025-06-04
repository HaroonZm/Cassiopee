# Demande à l'utilisateur de saisir trois valeurs séparées par des espaces et récupère la chaîne de caractères entrée
w, h, c = input().split()

# Convertit la première valeur w (largeur) en entier (typiquement utilisé pour déterminer le nombre de colonnes d'un cadre)
w = int(w)

# Convertit la deuxième valeur h (hauteur) en entier (typiquement utilisé pour déterminer le nombre de lignes d'un cadre)
h = int(h)

# Initialise une chaîne vide pour 'a' qui servira à représenter une ligne horizontale de tirets (le dessus/dessous du cadre)
a = ""

# Initialise une chaîne vide pour 'd' qui servira à représenter une ligne intérieure de points (le contenu du cadre)
d = ""

# Initialise une chaîne vide pour 'd_e' qui servira à représenter une ligne spéciale où un caractère 'c' sera inséré à la place d'un point
d_e = ""

# Initialise le compteur 'cnt' à 2. Ce compteur sera utilisé pour déterminer où placer le caractère spécial et contrôler les boucles
cnt = 2

# Boucle pour créer la partie centrale (horizontale) du cadre (largeur - 2 fois)
for i in range(w-2):
    # Incrémente le compteur de 1 à chaque itération (sert à repérer la position centrale)
    cnt += 1
    # Ajoute un tiret à la chaîne 'a' (sera utilisé pour la ligne du haut et du bas)
    a += "-"
    # Ajoute un point à la chaîne 'd' (sera utilisé pour les lignes intérieures standards)
    d += "."
    # Vérifie si la position actuelle n'est pas celle où le caractère spécial doit être inséré
    if cnt != w // 2 + 2:  # Le +2 ajuste la position pour correspondre à l’index voulu
        # Ajoute un point à 'd_e' tant que ce n'est pas la position du caractère spécial
        d_e += "."
    else:
        # Ajoute le caractère spécial 'c' à 'd_e' à la position centrale
        d_e += c

# Affiche la ligne du haut du cadre, composée d'un "+" suivi des tirets, puis un autre "+"
print("+" + a + "+")

# Réinitialise le compteur 'cnt' à 2 avant de traiter les lignes verticales
cnt = 2

# Boucle pour construire les lignes intérieures (hauteur - 2 fois)
for j in range(h-2):
    # Incrémente à chaque ligne pour suivre la position verticale
    cnt += 1
    # Si la ligne actuelle ne correspond pas à la position centrale (celle où placer la ligne spéciale)
    if cnt != h // 2 + 2:
        # Affiche la ligne standard avec des points : encadrée par des "|"
        print("|" + d + "|")
    else:
        # Affiche la ligne spéciale où le caractère 'c' remplace un point
        print("|" + d_e + "|")

# Affiche la ligne du bas du cadre, identique à celle du haut
print("+" + a + "+")