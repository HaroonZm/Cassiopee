# AOJ 1519: Room of Time and Spirit
# Python3 2018.7.13 bal4u
# Ce code implémente une structure d'ensemble union-find pondérée, et résout un problème où les poids sont modifiés et comparés via des opérations d'entrée/sortie.

# Définition d'une classe gérant une structure UNION-FIND pondérée (aussi appelé disjoint-set forest ou union-find avec gestion de potentiels)
class WeightedUnionSet:
    # Constructeur de la classe
    def __init__(self, nmax):
        # Initialisation d'une liste représentant le potentiel/poids de chaque élément (ici tous initialisés à zéro)
        self.ws = [0] * nmax
        # Initialisation du parent de chaque élément dans l'ensemble : chaque élément est à la base sa propre racine (-1 indique la racine)
        self.par = [-1] * nmax
        # Tableau pour mémoriser une valeur "de pouvoir" additionnelle propre à chaque élément (au début, tous à zéro)
        self.power = [0] * nmax

    # Méthode pour trouver la racine d'un élément x avec compression de chemin ET gestion du poids relatif jusqu'à la racine
    def find(self, x):
        # Si x est une racine (sa valeur parent est négative), alors la racine de x est x lui-même
        if self.par[x] < 0:
            return x
        # Appel récursif sur le parent de x pour trouver la racine ultime
        p = self.find(self.par[x])
        # Ajout du poids/w potentiel accumulé du parent à x (car on fait une compression de chemin avec propagation des potentiels)
        self.ws[x] += self.ws[self.par[x]]
        # Compression de chemin : le parent de x devient directement la racine trouvée (optimisation)
        self.par[x] = p
        # On renvoie alors la racine
        return p

    # Méthode pour obtenir le poids "absolu" de l'élément x (distance pondérée jusqu'à la racine, après compression de chemin)
    def weight(self, x):
        # On veille à ce que l'arbre soit compressé jusqu'à la racine
        self.find(x)
        # On renvoie la valeur du poids stockée pour x
        return self.ws[x]

    # Méthode pour tester si deux éléments x et y sont connectés, c'est-à-dire s'ils appartiennent au même ensemble racine
    def connected(self, x, y):
        # Si la racine de x est la même que celle de y, ils sont connectés
        return self.find(x) == self.find(y)

    # Méthode pour unir deux ensembles contenant x et y, avec prise en compte du décalage de poids w
    def unite(self, x, y, w):
        # On ajuste w : ajout du pouvoir pour x et son poids absolu
        w += self.power[x] + self.weight(x)
        # Retrait du pouvoir pour y et son poids absolu
        w -= self.power[y] + self.weight(y)
        # On trouve les racines respectives de x et y
        x, y = self.find(x), self.find(y)
        # Si les deux éléments sont déjà dans le même ensemble, rien à faire, on retourne 0
        if x == y:
            return 0
        # On assure que l'ensemble avec la plus petite taille est fusionné dans le plus gros
        # (plus la taille est négative, plus l'ensemble est gros car on stocke -taille dans par)
        if self.par[y] < self.par[x]:
            # On inverse x et y, et on inverse également le signe de w pour que le sens des potentiels soit cohérent
            x, y, w = y, x, -w
        # On additionne la taille des deux ensembles : taille de la nouvelle racine x = taille_x + taille_y
        self.par[x] += self.par[y]
        # y devient fils de x : par[y] = x
        self.par[y] = x
        # On fixe le poids associé à y par rapport à x (w donne la différence de potentiel entre y et x)
        self.ws[y] = w
        # L'union a bien eu lieu, on retourne 1
        return 1

    # Méthode pour obtenir la différence de poids entre x et y, à condition qu'ils appartiennent au même ensemble
    def diff(self, x, y):
        # Si x et y ne sont pas connectés, impossible de calculer la différence, on retourne [0, None]
        if self.find(x) != self.find(y):
            return [0, None]
        # Sinon, on retourne [1, différence], basée sur les poids pondérés
        return [1, self.ws[x] - self.ws[y]]

# Début du programme principal

# Lecture de deux entiers N (nombre d'éléments), Q (nombre de requêtes)
N, Q = map(int, input().split())
# Création de la structure de données, avec N+1 éléments (indices de 0 à N inclus)
u = WeightedUnionSet(N + 1)
# Lecture et traitement de chaque requête parmi les Q
for i in range(Q):
    # Lecture d'une ligne d'entrée, découpage en liste (q[0]=commande, q[1..]=paramètres)
    q = input().split()
    if q[0] == "IN":
        # Pour la requête "IN", on lit trois entiers a, b, c
        a, b, c = int(q[1]), int(q[2]), int(q[3])
        # On incrémente le pouvoir pour a de la quantité c
        u.power[a] += c
        # On incrémente aussi le pouvoir pour b de la quantité c
        u.power[b] += c
        # On fusionne les ensembles contenant a et b avec un décalage de poids c
        u.unite(a, b, c)
    else:
        # Pour toute requête autre, on suppose deux paramètres a, b
        a, b = int(q[1]), int(q[2])
        # On teste si a et b appartiennent au même sous-ensemble fusionné
        if u.find(a) != u.find(b):
            # Si non, on affiche un message d'avertissement
            print("WARNING")
        else:
            # Si oui, on calcule la différence de puissance totale entre b et a.
            # Cette différence inclut le pouvoir et le poids accumulé (i.e. potentiel) de chaque élément
            print((u.power[b] + u.ws[b]) - (u.power[a] + u.ws[a]))