import sys  # Le module sys fournit un accès à certaines variables utilisées ou maintenues par l'interpréteur.
import itertools  # Le module itertools propose diverses fonctions qui aident avec les itérations avancées.
# import numpy as np  # Ce code est commenté. Numpy est utilisé pour le calcul scientifique, mais il n'est pas utilisé ici.
import time  # Le module time offre des fonctions liées au temps. Ici, il n'est pas utilisé mais importé.
import math  # Le module math propose des fonctions mathématiques de base. Pas utilisé ici mais importé.

# Définit la limite maximale de récursion. Les appels récursifs peuvent provoquer un dépassement de pile,
# donc on élève la limite pour pouvoir gérer de grandes profondeurs de récursion si nécessaire.
sys.setrecursionlimit(10 ** 7)  # Définit la limite de récursion à 10 000 000.

from collections import defaultdict  # defaultdict est une sous-classe de dict qui appelle automatiquement une fonction pour fournir une valeur par défaut lorsque la clé n’existe pas.

# Les fonctions suivantes sont des raccourcis pour des lectures rapides de l'entrée standard binaire. 
read = sys.stdin.buffer.read  # Lit toute l'entrée standard et renvoie des octets.
readline = sys.stdin.buffer.readline  # Lit une ligne de l'entrée standard.
readlines = sys.stdin.buffer.readlines  # Lit toutes les lignes de l'entrée.

# Lecture de deux entiers sur la même ligne depuis l'entrée standard.
# Cette ligne utilise input(), qui lit une chaîne depuis l'entrée standard, split() divise la chaîne avec les espaces,
# map(int, ...) convertit chaque élément de la liste obtenue en entier, et le résultat est unpacké dans n et q.
n, q = map(int, input().split())  # n : nombre d'éléments, q : nombre de requêtes à traiter.

# Définition d'une classe de structure de données Union-Find (aussi appelée Disjoint Set Union/DSU),
# qui permet de gérer efficacement l'union de groupes et de vérifier si deux éléments sont dans le même groupe.
class UnionFind(object):
    # Constructeur de la classe, appelé à la création d'une nouvelle instance UnionFind.
    def __init__(self, n = 1):  # Le paramètre n représente le nombre d'éléments.
        # Chaque élément commence dans son propre groupe.
        # link[i] indique le parent immédiat de l'élément i. Au début, chaque élément est son propre parent (auto-boucle).
        self.link = [i for i in range(n)]  # Crée une liste où chaque élément pointe sur lui-même.
        # size[i] contient le nombre d'éléments dans le composant dont le représentant est i.
        self.size = [1 for _ in range(n)]  # Au début, chaque composant (chaque 'root') a une taille de 1.

    # Fonction pour trouver le représentant ("racine") du groupe auquel appartient l'élément x.
    # Implémente la compression de chemin : chaque nœud rencontré pointe directement sur la racine,
    # ce qui accélère les futurs appels à find(x).
    def find(self, x):
        # Si x est la racine du composant (il pointe vers lui-même), on retourne x.
        if self.link[x] == x:
            return x  # x est racine de son composant, on le retourne.

        # Sinon, on cherche récursivement la racine du parent de x, et on applique la compression de chemin,
        # c'est-à-dire que link[x] stocke directement le représentant de x.
        self.link[x] = self.find(self.link[x])
        return self.link[x]  # Retourne le représentant de x.

    # Vérifie si deux éléments x et y sont dans le même composant (même groupe)
    # en comparant leur représentant respectif.
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    # Réunit (fusionne) les groupes auxquels appartenent x et y.
    def unite(self, x, y):
        # On trouve la racine (le représentant) de x et de y.
        x = self.find(x)
        y = self.find(y)
        # Si x et y sont déjà dans le même groupe, on ne fait rien (ils sont déjà fusionnés).
        if x == y:
            return  # On quitte immédiatement, rien à fusionner.

        # Pour garder l'arbre le plus plat possible, on attache le plus petit groupe au plus grand.
        # Si la taille du groupe de x est inférieure à celle de y, on échange leur rôle.
        if self.size[x] < self.size[y]:
            x, y = y, x  # On échange les représentants, pour que x soit toujours le plus grand.
        self.link[y] = x  # On fait pointer la racine y vers x, fusionnant alors les deux groupes.
        self.size[x] += self.size[y]  # On met à jour la taille du nouveau groupe racine x.

    # Renvoie la taille du groupe auquel appartient x.
    def get_size(self, x):
        x = self.find(x)  # On trouve la racine de x.
        return self.size[x]  # On retourne la taille du groupe dont x est le représentant.

# Création d'une instance de la structure UnionFind avec n éléments.
u = UnionFind(n)
# On traite chaque requête disponible (il y en aura q en tout).
for i in range(q):
    # Lecture de trois entiers : com, x, y. Lecture via input(), split en liste, conversion chaque élément en int.
    # com détermine le type de requête :
    #   com == 0 : fusionner les groupes de x et y,
    #   com == 1 : vérifier si x et y sont dans le même groupe.
    com, x, y = map(int, input().split())
    if com == 0:
        # Requête de fusion : on demande à l'objet UnionFind de fusionner x et y.
        u.unite(x, y)
    else:
        # Requête de vérification : si x et y sont dans le même groupe, on affiche 1, sinon 0.
        print(1 if u.is_same(x, y) else 0)