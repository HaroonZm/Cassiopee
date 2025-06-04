# Nettoyage Robot 2.0 version débutant

# Directions pour se déplacer : haut, droite, bas, gauche
directions = [(-1,0), (0,1), (1,0), (0,-1)]
chiffre_vers_caractere = {0:'.', 1:'E'}

while True:
    # Lire les valeurs de n et k
    donnees = input().split()
    n = int(donnees[0])
    k = int(donnees[1])

    # Si n vaut 0, on arrête le programme
    if n == 0:
        break

    k = k - 1
    n1 = n - 1

    # Vérifier les conditions impossibles
    if (n % 2 == 1) or k >= (1 << (n // 2)):
        print("No\n")
        continue

    # Créer la grille
    grille = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(-1)
        grille.append(ligne)

    # Remplir la première ligne de la grille
    for colonne in range(n):
        shift = (n1 - colonne) // 2
        valeur = (k >> shift) & 1
        grille[0][colonne] = valeur

    # Remplir le reste de la grille
    for ligne in range(n1):
        for colonne in range(n):
            compteur = 0
            t = grille[ligne][colonne]
            for direction in directions:
                nouvelle_ligne = ligne + direction[0]
                nouvelle_colonne = colonne + direction[1]
                if (0 <= nouvelle_ligne < n) and (0 <= nouvelle_colonne < n):
                    if grille[nouvelle_ligne][nouvelle_colonne] == t:
                        compteur += 1
            if compteur == 2:
                grille[ligne+1][colonne] = 1 - t
            else:
                grille[ligne+1][colonne] = t

    # Afficher la grille
    for i in range(n):
        ligne_str = ""
        for j in range(n):
            ligne_str += chiffre_vers_caractere[grille[i][j]]
        print(ligne_str)
    print()