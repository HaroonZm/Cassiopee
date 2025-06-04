import math  # Importe le module mathématique pour utiliser des fonctions mathématiques, comme le logarithme
import sys  # Importe le module système pour obtenir des informations sur l'interpréteur Python

# Vérifie si la version de Python est la version 2
# sys.version renvoie une chaîne indiquant la version Python, ex: "3.8.10..."
# sys.version[0] == '2' vérifie donc si le premier caractère est '2' (donc Python 2.x)
if sys.version[0] == '2':
    # Si on est en Python 2 :
    # - On réassigne 'range' pour qu'il se comporte comme 'xrange', c'est-à-dire qu'il retourne un itérateur efficace en mémoire
    # - On réassigne 'input' pour qu'il se comporte comme 'raw_input', qui lit une chaîne de caractères sans évaluer
    range, input = xrange, raw_input

# Définition d'une classe nommée FenwickTree, qui représente un arbre de Fenwick (aussi appelé Binary Indexed Tree)
class FenwickTree:
    # Définition du constructeur (__init__) de la classe FenwickTree
    def __init__(self, a_list, f, default):
        # Cette classe est 0-indexée (« 0-indexed »)
        # En d'autres termes, les indices commencent à 0 au lieu de 1

        # Stockage de la taille du tableau d'entrée dans l'attribut d'instance N
        self.N = len(a_list)  # len(a_list) donne le nombre d'éléments dans a_list

        # Création d'une copie indépendante du tableau d'entrée pour servir de tableau de données « bit »
        self.bit = a_list[:]  # a_list[:] crée une copie superficielle de a_list pour éviter les effets de bord

        # Stockage de la fonction d'agrégation (comme max ou min) dans l'attribut d'instance f
        self.f = f

        # Stockage de la valeur par défaut utilisée pour « remplir » le tableau
        self.default = default

        # Calcul du nombre d'éléments à ajouter pour compléter la taille du tableau jusqu'à la prochaine puissance de deux
        # math.log(self.N, 2) calcule le logarithme base 2 de N
        # math.ceil arrondit à l'entier supérieur pour obtenir le nombre de bits nécessaire
        # 1 << x effectue un décalage binaire à gauche, équivalent à 2**x
        for _ in range(self.N, 1 << int(math.ceil(math.log(self.N, 2)))):
            # Ajoute la valeur par défaut à la fin du tableau jusqu'à ce que sa taille soit une puissance de deux
            self.bit.append(self.default)

        # Construction initiale de l'arbre de Fenwick
        # Cela permet de préparer la structure de données pour répondre efficacement aux requêtes
        for i in range(self.N - 1):
            # (i | (i + 1)) utilise l'opérateur OU binaire pour trouver le parent dans la structure de Fenwick
            # On applique la fonction d'agrégation f pour mettre à jour l'élément parent
            self.bit[i | (i + 1)] = self.f(self.bit[i | (i + 1)], self.bit[i])

    # Méthode pour appliquer une opération sur un élément du tableau, et propager la modification dans l'arbre
    def update(self, i, val):
        # Exécute tant que i est inférieur à N
        while i < self.N:
            # Met à jour le bit à la position i en appliquant la fonction d'agrégation
            self.bit[i] = self.f(self.bit[i], val)
            # Passe à l'indice parent dans le BIT grâce à l'opérateur ou binaire et l'incrémentation
            i |= i + 1  # équivalent à i = i | (i + 1)

    # Méthode pour effectuer une requête d'agrégation sur le préfixe [0, n], incluant le rang n
    def query(self, n):
        # Initialisation de la variable resultat (ret)
        # Ici, ret commence à 0 car c'est l'identité de max et la valeur par défaut
        ret = 0
        # On itère tant que n >= 0
        while n >= 0:
            # À chaque itération, on agrège le résultat courant avec la valeur du bit à l'indice n
            ret = self.f(ret, self.bit[n])
            # Mise à jour de n : (n & (n + 1)) donne le parent précédent dans l'arbre, puis on décrémente de 1
            n = (n & (n + 1)) - 1
        # Retourne le résultat agrégé sur le préfixe
        return ret

# On lit depuis l'entrée standard le nombre N, converti en entier
N = int(input())

# On lit la ligne suivante, la découpe sur les espaces avec split(), et convertit chaque élément en entier
X = [int(x) for x in input().split()]

# Création d'une instance de FenwickTree pour stocker les résultats de type DP (programmation dynamique)
# On initialise le tableau [0] * N, soit une liste de N zéros
# La fonction d'agrégation est max (on cherche le maximum)
# La valeur de base (default) est 0
dp = FenwickTree([0] * N, lambda x, y: max(x, y), 0)

# Pour chaque couple (x, i), où x est une valeur de X et i son indice dans X
# On trie les couples par valeur croissante de x
for x, i in sorted((x, i) for i, x in enumerate(X)):
    # On met à jour le FenwickTree à la position i
    # On cherche d'abord le maximum des préfixes jusqu'à i
    # On y ajoute x et on met à jour la valeur à la position i avec ce maximum augmenté de x
    dp.update(i, dp.query(i) + x)

# On calcule et affiche le résultat
# N * (N + 1) // 2 calcule la somme des entiers de 1 à N — somme de la suite arithmétique
# On soustrait dp.query(N - 1), qui retourne le meilleur score obtenu avec la DP
# print l'affiche à l'écran
print(N * (N + 1) // 2 - dp.query(N - 1))