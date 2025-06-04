# Première ligne : Récupérer les entrées de l'utilisateur
# La fonction input() lit une ligne au clavier en tant que chaîne de caractères (string)
# La méthode split() divise cette chaîne en une liste de sous-chaînes basées sur le séparateur espace par défaut
# On suppose que l'utilisateur saisit trois valeurs séparées par des espaces : la largeur, la hauteur et un caractère
W, H, c = input().split()

# Conversion de la largeur (W) de type string en type entier (int) pour permettre des opérations numériques ultérieures
W = int(W)
# Conversion de la hauteur (H) de type string en type entier (int)
H = int(H)
# La variable c reste une chaîne de caractères représentant un seul caractère

# Boucle extérieure : Parcourir chaque ligne du motif à afficher
# range(H) génère une séquence de nombres de 0 à H-1 (inclus), où chaque nombre représente un index de ligne
for i in range(H):
    # Boucle intérieure : Parcourir chaque colonne du motif pour la ligne actuelle
    # range(W) génère une séquence de nombres de 0 à W-1 (inclus), où chaque nombre représente un index de colonne
    for j in range(W):
        # Cas 1 : Le coin du motif (coin supérieur gauche, supérieur droit, inférieur gauche, inférieur droit)
        # Cette condition vérifie si nous sommes sur la première ou la dernière ligne (i==0 ou i==H-1)
        # ainsi qu'à la première ou la dernière colonne (j==0 ou j==W-1)
        if (i == 0 or i == H-1) and (j == 0 or j == W-1):
            # Afficher le caractère '+' pour les coins sans passer à la ligne suivante (end="" supprime le retour chariot)
            print("+", end="")
        # Cas 2 : Bordure horizontale (haut ou bas mais pas dans les coins)
        # Si nous sommes sur la première ou la dernière ligne (i==0 ou i==H-1) mais PAS dans les coins
        elif i == 0 or i == H-1:
            # Afficher le caractère '-' pour les bords horizontaux
            print("-", end="")
        # Cas 3 : Bordure verticale (gauche ou droite mais pas dans les coins)
        # Si nous sommes sur la première ou la dernière colonne (j==0 ou j==W-1) mais pas dans les coins ni sur les bords horizontaux
        elif j == 0 or j == W-1:
            # Afficher le caractère '|' pour les bords verticaux
            print("|", end="")
        # Cas 4 : Position spécifique pour le caractère c (typiquement au centre)
        # Cette condition vérifie si nous sommes exactement à la position centrale du motif
        # 2*i == H-1 et 2*j == W-1 assure que pour un motif de taille impaire, le 'c' soit bien centré
        elif 2*i == H-1 and 2*j == W-1:
            # Afficher le caractère c fourni par l'utilisateur
            print(c, end="")
        # Cas 5 : L'intérieur du motif, tous les autres cas
        else:
            # Afficher le caractère '.' pour remplir l'intérieur du motif
            print(".", end="")
    # Après avoir traité toutes les colonnes de la ligne courante, passer à la ligne suivante
    # La fonction print("") affiche juste un retour chariot pour passer à la ligne suivante
    print("")