def bomb(x, y):  # Définition de la fonction 'bomb' prenant en paramètres deux entiers x et y représentant des coordonnées sur une grille
    s = M[y]  # Attribution à la variable 's' de la chaîne de caractères correspondant à la ligne y dans la liste M, qui représente la grille
    if s[x] == "0":  # Condition vérifiant si le caractère à la position x de la ligne y est égal à "0"
        return  # Si c'est le cas, cela signifie qu'il n'y a rien à faire ici, donc on quitte la fonction immédiatement
    M[y] = s[:x] + "0" + s[x+1:]  # Remplacement du caractère à la position x de la ligne y par "0" : on construit une nouvelle chaîne où on conserve tout avant x, on met "0" à la position x, puis tout après x
    R = [-3, -2, -1, 1, 2, 3]  # Définition d'une liste R contenant des entiers positifs et négatifs représentant des décalages sur l'axe x ou y
    for e in R:  # Pour chaque élément e dans la liste R, on va effectuer des appels récursifs aux positions environnantes
        bomb(x + e, y)  # Appel récursif de la fonction bomb en décalant la coordonnée x de e, gardant y fixe, pour propager l'effet horizontalement
        bomb(x, y + e)  # Appel récursif de la fonction bomb en gardant x fixe, en décalant la coordonnée y de e, pour propager l'effet verticalement
    return  # Fin de la fonction, on retourne implicitement None

A = range(14)  # Création d'un objet range allant de 0 à 13 inclus, représentant des indices de lignes ou colonnes
B = range(3, 11)  # Création d'un objet range allant de 3 à 10 inclus, utilisé pour des indices spécifiques dans la grille
M = ["0" * 14 for i in A]  # Initialisation de la liste M avec 14 chaînes de caractères, chacune composée de 14 caractères "0", représentant une grille 14x14 remplie de "0"
z = "000"  # Définition de la chaîne de caractères 'z' composée de trois caractères "0", utilisée pour le padding
N = range(input())  # Création d'un range dont la taille est donnée par un entier fourni par l'utilisateur (nombre de cas à traiter)

for i in N:  # Boucle sur chaque élément i de N (de 0 à nombre de cas - 1)
    s = raw_input()  # Lecture d'une chaîne de caractères entrée par l'utilisateur (variable apparemment non utilisée par la suite)
    for j in B:  # Boucle sur les indices j de la plage B (de 3 à 10)
        M[j] = z + raw_input() + z  # Lecture d'une ligne de la grille (user input), préfixée et suffixée par "000" pour former une ligne de longueur 14
    x = input() + 2  # Lecture de la coordonnée x entrée par l'utilisateur, à laquelle on ajoute 2 pour compenser le décalage dû au padding 'z'
    y = input() + 2  # Lecture de la coordonnée y entrée par l'utilisateur, également décalée de +2 pour la même raison
    bomb(x, y)  # Appel de la fonction bomb avec les coordonnées ajustées pour déclencher la modification dans la grille
    print "Data %d:" % (i + 1)  # Affichage d'un entête indiquant le numéro du cas traité, en commençant à 1
    for j in B:  # Boucle sur les lignes indices dans B
        print M[j][3:-3]  # Impression de chaque ligne j de la grille M en enlevant le padding de trois "0" de chaque côté, afin d'afficher la grille d'origine après modifications