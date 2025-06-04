# Définition d'une classe Matrix qui représente une matrice et prend en charge
# diverses opérations de matrices, y compris l'addition, la multiplication,
# l'exponentiation puissance entière, avec support du modulo.
class Matrix():
    # Variable de classe utilisée pour définir la valeur du modulo appliqué aux éléments de la matrice
    mod = 10 ** 9 + 7   # Le modulo est typiquement utilisé pour éviter les entiers trop grands

    # Méthode statique permettant de changer dynamiquement la valeur du modulo
    # Cette méthode modifie la variable de classe 'mod' pour toutes les instances de Matrix
    def set_mod(m):
        Matrix.mod = m

    # Constructeur de la classe Matrix, prend une liste de listes L représentant les valeurs
    # de la matrice à deux dimensions
    def __init__(self, L):
        # Nombre de lignes dans la matrice, obtenu en prenant la longueur de la liste L
        self.row = len(L)
        # Nombre de colonnes dans la matrice, obtenu en prenant la longueur de la première sous-liste de L
        self.column = len(L[0])
        # Copie de la matrice réelle, pour garder les valeurs et les manipuler plus tard
        self._matrix = L
        # Boucle pour appliquer le modulo à chaque élément de la matrice
        for i in range(self.row):
            for j in range(self.column):
                self._matrix[i][j] %= Matrix.mod  # Le modulo est appliqué à chaque élément

    # Méthode spéciale permettant d'accéder à un élément individuel de la matrice via l'opérateur []
    # Attend un tuple (i, j) représentant les indices de ligne et de colonne
    def __getitem__(self, item):
        # Si l'utilisateur passe un seul entier au lieu d'un tuple (par exemple mat[1])
        if type(item) == int:
            raise IndexError("you must specify row and column")  # Erreur explicite
        # Si l'utilisateur ne fournit pas exactement deux indices
        elif len(item) != 2:
            raise IndexError("you must specify row and column")

        i, j = item  # Décomposition du tuple en indices ligne et colonne
        return self._matrix[i][j]  # Retourne l'élément à la position (i, j)

    # Méthode spéciale permettant de modifier un élément individuel de la matrice via l'opérateur []
    def __setitem__(self, item, val):
        # Même contrôles qu'à la lecture pour s'assurer que l'accès est valide
        if type(item) == int:
            raise IndexError("you must specify row and column")
        elif len(item) != 2:
            raise IndexError("you must specify row and column")

        i, j = item  # Indices de ligne et colonne
        self._matrix[i][j] = val  # Modification de l'élément ciblé

    # Surcharge de l'opérateur + pour ajouter deux matrices de même dimensions
    def __add__(self, other):
        # On vérifie que les deux matrices ont la même dimension (sinon on renvoie une erreur)
        if (self.row, self.column) != (other.row, other.column):
            raise SizeError("sizes of matrices are different")  # Custom erreur non définie ici

        # On crée une nouvelle matrice résultat remplie de zéros, de même dimension que les matrices additionnées
        res = [[0 for j in range(self.column)] for i in range(self.row)]
        # Double boucle pour parcourir toutes les positions de la matrice
        for i in range(self.row):
            for j in range(self.column):
                # On additionne les éléments, puis on applique le modulo
                res[i][j] = self._matrix[i][j] + other._matrix[i][j]
                res[i][j] %= Matrix.mod  # Application du modulo

        # Création d'une nouvelle instance de Matrix avec la matrice additionnée
        return Matrix(res)

    # Surcharge de l'opérateur * pour permettre la multiplication (matricielle ou scalaire selon le type)
    def __mul__(self, other):
        # Cas où 'other' n'est pas un entier : on réalise la multiplication matricielle standard
        if type(other) != int:
            # On vérifie la compatibilité des dimensions pour la multiplication (colonnes de A = lignes de B)
            if self.column != other.row:
                raise SizeError("sizes of matrices are different")
            # Création d'une matrice résultat de la dimension correcte, initialisée à 0
            res = [[0 for j in range(other.column)] for i in range(self.row)]
            # On réalise la multiplication matricielle triple boucle standard
            for i in range(self.row):
                for j in range(other.column):
                    temp = 0  # Variable temporaire pour stocker la somme
                    for k in range(self.column):
                        temp += self._matrix[i][k] * other._matrix[k][j]  # Multiplication accrochée
                    res[i][j] = temp % Matrix.mod  # Application du modulo sur le résultat
            return Matrix(res)  # On retourne la nouvelle matrice
        else:
            # Cas où 'other' est un entier : multiplication scalaire (chaque élément est multiplié par l'entier)
            n = other  # On stocke l'entier dans une variable
            # On construit la nouvelle matrice en multipliant chaque élément par n et en appliquant le modulo
            res = [[(n * self._matrix[i][j]) % Matrix.mod for j in range(self.column)] for i in range(self.row)]
            return Matrix(res)  # On retourne la matrice scalaire multipliée

    # Surcharge de l'opérateur ** pour permettre l'exponentiation d'une matrice à une puissance entière
    def __pow__(self, m):
        # L'exponentiation n'est définie que pour les matrices carrées (autant de lignes que de colonnes)
        if self.column != self.row:
            raise MatrixPowError("the size of row must be the same as that of column")
        n = self.row  # On récupère la taille de la matrice carrée
        # Création de la matrice identité de taille n x n
        res = Matrix([[int(i == j) for i in range(n)] for j in range(n)])
        # Exponentiation rapide par dichotomie classique
        while m:
            if m % 2 == 1:
                res = res * self  # Multiplie la matrice résultat par la matrice courante si m est impair
            self = self * self  # On élève la matrice au carré
            m //= 2  # On divise m par 2 pour continuer
        return res  # On retourne la matrice obtenue

    # Méthode pour afficher une matrice sous forme de chaîne (utile pour print())
    def __str__(self):
        res = []  # On utilise une liste pour construire la chaîne de caractères finale
        for i in range(self.row):
            for j in range(self.column):
                res.append(str(self._matrix[i][j]))  # On convertit chaque élément en chaîne
                res.append(" ")  # On ajoute un espace entre les éléments
            res.append("\n")  # Saut de ligne à la fin de chaque ligne de la matrice
        res = res[:len(res)-1]  # On retire le dernier saut de ligne ajouté en trop
        return "".join(res)  # On fusionne tous les éléments de la liste en une seule chaîne

# Lecture des entrées utilisateur séparées par des espaces.
# On stocke dans N le premier entier et dans M le second.
N, M = map(int, input().split())

# Lecture des entiers dans une ligne suivante pour constituer la liste X
X = list(map(int, input().split())) + [N]  # On ajoute la valeur N à la fin de la liste

# Initialisation d'une liste dp de M+2 éléments, tous à 0, utilisée pour la programmation dynamique
dp = [0] * (M + 2)

# On initialise le premier élément de dp à 1 (cas de base de la programmation dynamique)
dp[0] = 1

# Définition de la matrice A
# Il s'agit ici d'une matrice 3x3, utilisée dans la récurrence
A = Matrix([[4, -2, 1],
            [1, 0, 0],
            [0, 1, 0]])

# Définition de la matrice colonne DP, initialisée à [0, 0, 0]
DP = Matrix([[0], [0], [0]])

# Variable 'first' initialisée à 0, utilisée pour suivre la position précédente traitée
first = 0

# Définition d'une matrice base colonne, utilisée dans le calcul récurrent
base = Matrix([[5], [1], [0]])

# Boucle de 1 à M+2 (inclus)
for i in range(1, M + 2):
    # On élève la matrice A à la puissance (X[i-1] - first)
    # Puis, on multiplie cette puissance de la matrice à une expression dépendant de DP et dp[i-1]
    # DP + base * (-dp[i-1]) signifie qu'on ajoute à DP le produit de base par moins dp[i-1]
    DP = (A ** (X[i - 1] - first)) * (DP + base * (-dp[i - 1]))
    # On extrait la valeur du troisième élément de DP (indice 2,0) et on la stocke dans dp[i]
    dp[i] = DP[2, 0]
    first = X[i - 1]  # On met à jour la position "first" courante

# À la fin, on affiche la quantité -dp[-1] modulo 1e9+7 (le résultat final du calcul)
print((-dp[-1]) % (10 ** 9 + 7))