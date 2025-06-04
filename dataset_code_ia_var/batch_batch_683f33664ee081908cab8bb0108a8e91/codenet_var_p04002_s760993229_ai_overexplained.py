import sys  # Importe le module sys, qui fournit l'accès à certaines fonctions système telles que la gestion de l'entrée/sortie

input = sys.stdin.readline  # Assigne à 'input' la fonction permettant de lire une ligne à partir de l'entrée standard (rapide pour les grands volumes)

# Lit une ligne de l'entrée standard, la découpe en morceaux selon les espaces, convertit chaque morceau en int, puis les assigne à W, H, N
# W : largeur de la grille, H : hauteur de la grille, N : nombre de points marqués ('noircis')
W, H, N = map(int, input().split())

vs = set()  # Initialise 'vs' comme un ensemble (set) vide pour stocker les points marqués, sans doublons

for _ in range(N):  # Boucle N fois pour lire les coordonnées des points à marquer
    a, b = map(int, input().split())  # Lit deux entiers sur une ligne, représente la position (a, b)
    vs.add((a-1, b-1))  # Ajoute à l'ensemble 'vs' le point, en convertissant à une indexation basée à 0 pour Python

R = [0] * 10  # Crée une liste 'R' de 10 zéros, chaque case représentera le nombre de sous-grilles 3x3 ayant respectivement 0,1,...,9 cases marquées

vvs = set()  # Crée un ensemble pour mémoriser les positions (x, y) des sous-grilles 3x3 déjà comptabilisées, pour éviter doubles-comptes

# Parcourt chaque point marqué
for a, b in vs:
    # On cherche autour de chaque point marqué toutes les sous-grilles 3x3 qui pourraient contenir ce point.
    # Pour chaque décalage possible dans une fenêtre 3x3, on considère (x, y) comme coin supérieur gauche de sous-grille 3x3
    for i in range(3):  # Variation de la ligne : 0, 1, 2
        for j in range(3):  # Variation de la colonne : 0, 1, 2
            x = a + i - 2  # Calcule la coordonnée x du coin supérieur gauche
            y = b + j - 2  # Calcule la coordonnée y du coin supérieur gauche

            # Vérifie si la sous-grille 3x3 sort du cadre de la grille principale
            # Si x < 0 ou y < 0, la sous-grille déborde à gauche ou en haut
            # Si x > W-3 ou y > H-3, elle déborde à droite ou en bas (W-3, H-3 sont les limites valides)
            if x < 0 or W-3 < x or y < 0 or H-3 < y:
                continue  # Ignore ce cas, on passe au prochain décalage

            if (x, y) in vvs:  # Si cette sous-grille a déjà été comptée, on passe
                continue

            c = 0  # Compteur du nombre de cases marquées dans la sous-grille courante

            # On parcourt chaque case k,l de la sous-grille 3x3 démarrant à (x, y)
            for k in range(3):  # k : 0, 1, 2
                for l in range(3):  # l : 0, 1, 2
                    # Si la case (x + k, y + l) appartient à l'ensemble des cases marquées
                    if (x + k, y + l) in vs:
                        c += 1  # On ajoute 1 au compteur

            R[c] += 1  # On incrémente le nombre de sous-grilles contenant 'c' cases marquées
            vvs.add((x, y))  # On marque cette sous-grille comme déjà comptée pour ne pas la recompter plus tard

# Une fois toutes les sous-grilles comportant au moins un point marqué comptées, il reste à remplir R[0] (= sous-grilles sans aucun point marqué)
# Le nombre total possible de sous-grilles 3x3 dans la grille principale est (H-2)*(W-2)
# On soustrait à ce total la somme des sous-grilles où il y a au moins un point marqué (qui a rempli R[1] à R[9])
R[0] = (H - 2) * (W - 2) - sum(R)

# Affichage du résultat pour chaque nombre de cases marquées (de 0 à 9)
for i in range(10):  # Pour chaque indice de 0 à 9
    print(R[i])  # Affiche le nombre de sous-grilles 3x3 qui contiennent exactement i cases marquées