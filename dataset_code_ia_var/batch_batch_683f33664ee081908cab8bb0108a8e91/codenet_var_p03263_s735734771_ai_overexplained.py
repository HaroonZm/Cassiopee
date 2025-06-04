# On commence par lire deux entiers depuis l'entrée standard
# input() lit une ligne de texte, .split() la découpe en éléments séparés, map(int, ...) convertit chaque élément en entier
# H représente le nombre de lignes (hauteur), W le nombre de colonnes (largeur)
H, W = map(int, input().split())

# On initialise une liste vide dans laquelle chaque élément sera une sous-liste représentant une ligne de la grille
# On fait une boucle qui s'exécute H fois (pour chaque ligne)
# À chaque itération : on lit une ligne, on split la ligne, on convertit chaque élément en int, on forme une liste
# Puis on ajoute cette liste à la liste globale 'a' qui représente toute la grille
a = []
for i in range(H):  # 'i' varie de 0 à H-1 (chaque ligne)
    # On lit la ligne entière, on convertit tous les éléments en entier, et on crée la sous-liste
    ligne = list(map(int, input().split()))
    a.append(ligne)  # Ajout de la sous-liste à la liste principale

# On initialise la liste 'ans', qui va stocker la liste des opérations effectuées
ans = []

# On parcourt chaque élément de la grille sauf la dernière colonne
# Cette double boucle permet de visiter chaque case (i,j) sauf tout à droite
for i in range(H):  # Pour chaque ligne, 'i' de 0 à H-1
    for j in range(W-1):  # Pour chaque colonne sauf la dernière, 'j' de 0 à W-2
        # Si la valeur de la case courante est impaire (test sur le reste modulo 2)
        if a[i][j] % 2 == 1:
            # On enregistre l'opération : déplacer 1 unité de (i,j) à (i,j+1)
            # Les indices sont incrémentés de 1 pour l'affichage (indices humains, commencent à 1)
            ans.append([i+1, j+1, i+1, j+2])
            # On ajoute 1 à la case suivante (colonne à droite du curseur)
            a[i][j+1] += 1

# Après avoir effectué le déplacement vers la droite dans chaque ligne,
# Il reste potentiellement des valeurs impaires dans la dernière colonne
# On parcourt chaque ligne sauf la dernière pour gérer les valeurs impaires dans la dernière colonne
for i in range(H-1):  # 'i' de 0 à H-2
    # Si la dernière case de la ligne courante est impaire
    if a[i][W-1] % 2 == 1:
        # On effectue une opération de transfert vers la case du dessous (même colonne, ligne suivante)
        ans.append([i+1, W, i+2, W])  # Toujours indices +1 pour affichage humain
        # On ajoute 1 à la case du dessous
        a[i+1][W-1] += 1

# On affiche le nombre total d'opérations enregistrées dans 'ans'
print(len(ans))

# On affiche chaque opération une par une sous forme de quatre nombres entiers
# On décompose chaque liste de 'ans' dans les variables a, b, c, d (qui correspondent aux coordonnées)
for a, b, c, d in ans:
    print(a, b, c, d)