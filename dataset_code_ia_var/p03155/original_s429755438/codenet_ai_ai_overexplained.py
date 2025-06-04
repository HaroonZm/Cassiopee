# Demande à l'utilisateur de saisir un entier pour N, qui représente probablement la taille (par exemple, la taille d'un carré ou d'un rectangle)
N = int(input())  # input() récupère une chaîne de caractères depuis l'utilisateur, puis int() convertit cette chaîne en un nombre entier

# Demande à l'utilisateur de saisir un entier pour H, qui représente probablement la hauteur d'un sous-rectangle à placer dans la zone de taille N
H = int(input())  # Encore une saisie de l'utilisateur suivie d'une conversion en entier

# Demande à l'utilisateur de saisir un troisième entier pour W, qui représente probablement la largeur d'un sous-rectangle à placer dans la zone de taille N
W = int(input())  # Même procédé : saisie utilisateur puis conversion en entier

# Calcule combien de positions différentes un rectangle de hauteur H et de largeur W peut occuper dans un carré de taille N x N
# Premièrement, (N - H + 1) donne le nombre de positions verticales possibles (lignes où le haut du rectangle peut se placer sans dépasser la zone)
# Deuxièmement, (N - W + 1) donne le nombre de positions horizontales possibles (colonnes où le côté gauche du rectangle peut se placer sans dépasser la zone)
# Le produit des deux donne le nombre total de positions possibles où le rectangle s'insère entièrement dans la zone
resultat = (N - H + 1) * (N - W + 1)  # Calcul du nombre total de façons de placer le sous-rectangle

# Affiche le résultat du calcul précédent à l'écran
print(resultat)  # print() affiche la valeur de 'resultat' dans le terminal pour que l'utilisateur puisse voir le résultat