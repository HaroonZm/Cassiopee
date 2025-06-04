from heapq import heappop, heappush
from collections import Counter

class Node:
    """
    Représente un nœud dans l'arbre de Huffman.
    Chaque nœud possède un poids (fréquence d'apparition du caractère associé),
    un parent (optionnel, défini lors de la construction de l'arbre), et des méthodes
    pour récupérer la profondeur et le poids du nœud.
    """
    def __init__(self, weight):
        """
        Initialise un nœud avec un poids donné.
        Args:
            weight (int): Le poids (fréquence) du nœud.
        """
        self.weight = weight
        self.parent = None
        
    def set_parent(self, parent):
        """
        Associe un parent au nœud courant.

        Args:
            parent (Node): Le nœud parent.
        """
        self.parent = parent
        
    def get_length(self):
        """
        Calcule récursivement la profondeur du nœud dans l'arbre
        (nombre d'arêtes jusqu'à la racine).

        Returns:
            int: Profondeur du nœud courant.
        """
        try:
            tmp = 1 + self.parent.get_length()
        except AttributeError:
            tmp = 0
        return tmp
        
    def get_weight(self):
        """
        Retourne le poids (fréquence) du nœud.

        Returns:
            int: Poids du nœud.
        """
        return self.weight

    def __lt__(self, other):
        """
        Compare deux nœuds selon leur poids, requis pour l'utilisation dans un tas (heap).

        Args:
            other (Node): L'autre nœud à comparer.

        Returns:
            bool: True si le poids du nœud courant est inférieur à celui de l'autre nœud.
        """
        return self.weight < other.weight
    

# Lecture de la chaîne d'entrée
S = input()

# Calcul de la fréquence d'apparition de chaque caractère dans la chaîne
d = Counter(S)

# Dictionnaire pour stocker les nœuds de l'arbre
tree_dic = {}

# Liste (heap) utilisée pour la construction de l'arbre de Huffman
h = []

# Compteur unique pour nommer les nœuds internes
num = 0

# Création de feuilles pour chaque caractère unique et insertion dans le heap
for i in d:
    tree_dic[i] = Node(d[i])
    heappush(h, tree_dic[i])

# Construction de l'arbre de Huffman à l'aide d'un heap prioritaire
while len(h) > 1:
    # On retire les deux nœuds ayant les plus petites fréquences
    tmp0 = heappop(h)
    tmp1 = heappop(h)
    
    # Création d'un nouveau nœud interne avec pour poids la somme des deux plus petits
    tree_dic[num] = Node(tmp0.get_weight() + tmp1.get_weight())
    
    # On définit les parents pour les deux précédents nœuds extraits
    tmp0.set_parent(tree_dic[num])
    tmp1.set_parent(tree_dic[num])
    
    # On remet le nouveau nœud dans le heap
    heappush(h, tree_dic[num])
    num += 1

# Calcul de la longueur totale des codes attribués à chaque caractère
ans = 0
for i in S:
    ans += tree_dic[i].get_length()

# Cas particuliers : chaîne de longueur 1 ou composée d'un seul caractère unique
if len(S) == 1:
    print(1)
elif len(d) == 1:
    print(len(S))
else:
    print(ans)