# Déclaration de la classe RMQ (Range Maximum Query), qui implémente une structure de segment tree pour effectuer des requêtes de maximum sur des intervalles et des mises à jour de valeurs
class RMQ:
    # Définition d'une variable de classe appelée 'inf' qui sert ici comme valeur "neutre" pour le max (ici 0 car on travaille avec max, ce qui est douteux pour l'appellation inf)
    inf = 0

    # Méthode d'initialisation du RMQ, appelée lors de la création d'une instance.
    # Prend un seul argument n_ qui représente la taille initiale des données à stocker.
    def __init__(self, n_):
        # Stocke la taille initiale passée en argument dans un attribut d'instance.
        self.n_ = n_
        # self.n sera ajusté pour devenir la plus petite puissance de deux supérieure ou égale à n_.
        self.n = 1
        # On ajuste self.n à la puissance de deux supérieure ou égale à n_. 
        # On utilise une boucle while : tant que self.n < n_, on multiplie self.n par 2.
        while self.n < n_:
            self.n *= 2
        # On crée un tableau de segment (segment tree) initialisé avec des zéros (valeur de self.inf).
        # Sa taille est de 2*self.n-1 pour contenir tous les noeuds internes et feuilles du segment tree complet.
        self.st = [self.inf] * (2 * self.n - 1)

    # Méthode pour mettre à jour la valeur d'un élément à la position k dans le segment tree avec une nouvelle valeur x.
    def update(self, k, x):
        # On convertit l'indice de l'élément (k) en indice correspondant à une feuille du segment tree.
        # Les feuilles correspondent aux indices allant de self.n-1 à 2*self.n-2 dans self.st.
        k += (self.n - 1)
        # On place la nouvelle valeur x à la position de la feuille dans le tableau du segment tree.
        self.st[k] = x
        # On remonte dans l'arbre pour mettre à jour les valeurs maximales des noeuds parents.
        while k > 0:
            # On obtient l'indice du parent en utilisant la formule (k-1)//2.
            k = (k - 1) // 2
            # On met à jour la valeur du parent avec le maximum de ses deux enfants.
            self.st[k] = max(self.st[2 * k + 1], self.st[2 * k + 2])

    # Méthode récursive qui effectue une requête de maximum dans l'intervalle [a, b) sur le sous-arbre raciné en k,
    # représentant l'intervalle [l, r)
    def search(self, a, b, k, l, r):
        # Si l'intervalle interrogé [a, b) et l'intervalle du noeud courant [l, r) ne se chevauchent pas,
        # on retourne la valeur neutre (0 dans notre cas).
        if r <= a or b <= l:
            return self.inf
        # Si l'intervalle [l, r) du noeud courant est inclus dans [a, b), on retourne sa valeur maximale pré-computée.
        if a <= l and r <= b:
            return self.st[k]
        # Sinon, on découpe l'intervalle courant en deux et on fait deux appels récursifs à gauche et à droite.
        # Pour les enfants, on ajuste les bornes de l'intervalle et les indices k du noeud.
        # Le fils gauche est à k*2+1, couvre [l, (l+r)//2)
        L = self.search(a, b, k * 2 + 1, l, (l + r) // 2)
        # Le fils droit est à k*2+2, couvre [(l+r)//2, r)
        R = self.search(a, b, k * 2 + 2, (l + r) // 2, r)
        # On retourne le maximum entre les deux moitiés.
        return max(L, R)

    # Méthode plus simple qui permet à l'utilisateur de faire une requête de maximum sur l'intervalle [a, b)
    # sans avoir à manipuler les indices internes du segment tree.
    def query(self, a, b):
        # Lance la recherche à partir de la racine du segment tree (k=0, [0, self.n))
        return self.search(a, b, 0, 0, self.n)

# Lecture du nombre d'éléments n depuis l'entrée standard, via la fonction input().
n = int(input())
# Lecture de n entiers depuis la ligne suivante, conversion avec map vers des entiers, puis transformation en liste.
x = list(map(int, input().split()))
# Création d'une instance de RMQ sur n+1 éléments (pour gérer les indices jusqu'à n inclus).
rmq = RMQ(n + 1)
# Boucle sur chaque élément i de la liste x (c'est-à-dire pour chaque valeur d'entrée).
for i in x:
    # Pour chaque i, on interroge le RMQ pour obtenir le maximum dans l'intervalle [1, i).
    # Cela donne la plus grande somme atteignable strictement avant la position i.
    res = rmq.query(1, i)
    # On met à jour la position i dans le RMQ avec i + res, qui représente la nouvelle somme atteignable en choisissant i après la meilleure sous-séquence se terminant avant i.
    rmq.update(i, i + res)
# Après la boucle, on calcule la somme de tous les éléments x, puis on soustrait la valeur maximale atteinte dans l'intervalle [1, n+1).
# Cela donne la somme minimale à retirer pour obtenir la plus grande somme de sous-séquence croissante, c'est une transformation connue (exercice classique du LIS pondéré).
print(sum(x) - rmq.query(1, n + 1))