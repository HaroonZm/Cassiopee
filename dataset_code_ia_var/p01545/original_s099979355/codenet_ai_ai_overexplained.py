import math  # Importe le module math pour pouvoir utiliser des fonctions mathématiques avancées, comme log, ceil, etc.
import sys  # Importe le module sys pour accéder à certains paramètres et fonctions liés à l'interpréteur Python

# Cette condition vérifie si le script s'exécute sur Python 2.
if sys.version[0] == '2':  # sys.version est une chaîne représentant la version de Python utilisée. Le caractère à l'indice 0 correspond à la version majeure ('2' ou '3')
    range, input = xrange, raw_input  # En Python 2, 'range' crée une liste et 'xrange' renvoie un générateur avec un comportement plus économe en mémoire. 'input' équivaut à 'raw_input' pour la saisie utilisateur.

# Définition d'une classe FenwickTree, également appelée arbre de Fenwick ou Binary Indexed Tree, une structure de données efficace pour certains types de requêtes et de modifications sur des tableaux.
class FenwickTree:
    # La méthode __init__ initialise une nouvelle instance de FenwickTree
    def __init__(self, a_list, f, default):
        # a_list : Liste de valeurs sur lesquelles l'arbre va opérer.
        # f : Fonction d'agrégation (par exemple, max, somme, min, etc.).
        # default : Valeur neutre pour l'opération (pour max : 0, pour somme : 0, pour min : +inf, etc.).

        # La taille du tableau initial est stockée dans self.N
        self.N = len(a_list)  # Nombre d'éléments d'origine
        self.bit = a_list[:]  # Copie le tableau passé en paramètre pour l'utiliser comme structure sous-jacente de l'arbre.
        self.f = f  # Stocke la fonction d'agrégation pour une utilisation ultérieure.
        self.default = default  # Stocke la valeur neutre.

        # Complète l'arbre avec la valeur neutre pour que sa taille soit une puissance de 2 supérieure ou égale à N (utile pour certains algorithmes).
        for _ in range(self.N, 1 << int(math.ceil(math.log(self.N, 2)))):  # 1 << k équivaut à 2^k. math.log(self.N, 2) prend le logarithme base 2 de N.
            self.bit.append(self.default)  # Ajoute la valeur par défaut à chaque itération pour atteindre une puissance de 2

        # Met à jour les valeurs de l'arbre de Fenwick pour préparer la construction.
        for i in range(self.N - 1):  # Parcourt tous les indices sauf le dernier.
            idx = i | (i + 1)  # i | (i + 1) est une opération binaire pour obtenir l'index du parent/jumeau dans l'arbre.
            # Met à jour la valeur à l'indice idx en utilisant la fonction d'agrégation sur la valeur actuelle et la valeur à l'indice i.
            self.bit[idx] = self.f(self.bit[idx], self.bit[i])

    # Méthode pour mettre à jour la valeur à l'indice i en y appliquant la fonction d'agrégation avec 'val'
    def update(self, i, val):
        # Tant que l'indice i est valide (inférieur à la taille N d'origine)
        while i < self.N:
            self.bit[i] = self.f(self.bit[i], val)  # Met à jour la valeur à l'indice i en utilisant la fonction f
            i |= i + 1  # Passe à l'indice suivant qui doit être mis à jour d'après l'arbre de Fenwick (ajoute les bits de poids faible)

    # Méthode pour calculer l'agrégation des valeurs allant de l'indice 0 à n inclus
    def query(self, n):
        # [0, n]
        ret = 0  # Initialise le résultat d'accumulation à 0 (fonctionne si la valeur neutre pour max est 0)
        while n >= 0:  # Continue tant que l'indice est dans les bornes du tableau
            ret = self.f(ret, self.bit[n])  # Agrège la valeur à l'indice n avec le résultat courant en utilisant f
            n = (n & (n + 1)) - 1  # Passe à l'indice du parent dans la représentation de l'arbre de Fenwick
        return ret  # Renvoie le résultat de l'agrégation

# Lis une entrée en la convertissant en entier. Cela représente le nombre total d'éléments (taille du tableau)
N = int(input())  # input() lit une chaîne depuis l'entrée standard ; int() la convertit en entier

# Lis une ligne d'entrées, la découpe en sous-chaînes puis les convertit toutes en entiers
X = [int(x) for x in input().split()]  # input().split() crée une liste de mots, pour chaque mot on le convertit en entier

# Instancie un objet FenwickTree pour résoudre le problème.
# Le tableau initial contient N zéros : [0, ..., 0]
# La fonction d'agrégation est le maximum entre deux valeurs (lambda x, y: max(x, y))
# La valeur neutre (pour max) est 0
dp = FenwickTree([0] * N, lambda x, y: max(x, y), 0)

# Pour chaque valeur x et son indice i, triés par x croissant
for x, i in sorted((x, i) for i, x in enumerate(X)):
    # Pour chaque élément, on met à jour le FenwickTree à la position i avec la valeur 'dp.query(i) + x'
    # Cela permet de calculer le sous-ensemble croissant de la somme maximale se terminant à i
    dp.update(i, dp.query(i) + x)

# Calcule la somme totale des indices de 1 à N, soit N*(N+1)//2, puis retire la valeur dp.query(N-1) correspondant à l'agrégation maximale jusqu'au dernier index.
print(N * (N + 1) // 2 - dp.query(N - 1))  # Affiche le résultat final, qui dépend de la logique métier du problème (par exemple, différence entre somme maximale et une certaine valeur optimale)