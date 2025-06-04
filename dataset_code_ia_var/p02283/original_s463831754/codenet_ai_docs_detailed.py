import sys

NIL = -1  # Special sentinel value representing a non-existent or null node.

class Node:
    """
    Classe représentant un nœud dans un arbre binaire de recherche.

    Attributs :
        key (int): La clé ou la valeur stockée dans le nœud.
        parent (Node ou int): Référence au parent du nœud ou NIL si aucun.
        left (Node ou int): Référence au fils gauche ou NIL si aucun.
        right (Node ou int): Référence au fils droit ou NIL si aucun.
    """
    def __init__(self, key):
        """
        Initialise un nouveau nœud avec une clé donnée.

        Args:
            key (int): La valeur à stocker dans le nœud.
        """
        self.key = key
        self.parent = NIL
        self.left = NIL
        self.right = NIL

class Tree:
    """
    Classe représentant un arbre binaire de recherche (BST).

    Attributs :
        root (Node ou int): Racine de l'arbre ou NIL si l'arbre est vide.
    """
    def __init__(self):
        """
        Initialise un nouvel arbre binaire vide.
        """
        self.root = NIL

    def insert(self, z):
        """
        Insère un nouveau nœud dans l'arbre selon les règles du BST.

        Args:
            z (Node): Le nœud à insérer dans l'arbre. Les attributs parent, left et right seront initialisés ici.
        """
        y = NIL    # y sera le futur parent de z après la boucle
        x = self.root

        # Parcours l'arbre pour trouver l'emplacement d'insertion
        while x != NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        # y pointe sur le parent qui devient le parent du nouveau nœud
        z.parent = y

        # Si l'arbre est vide, z devient la racine
        if y == NIL:
            self.root = z
        # Sinon, z devient le fils gauche ou droit selon la valeur de sa clé
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def inorder_walk(self, node):
        """
        Parcours l'arbre en ordre croissant (gauche, racine, droite) en commençant par un nœud donné.
        Affiche les clés sans les retourner.

        Args:
            node (Node ou int): Nœud à partir duquel commencer le parcours. Peut être NIL.
        """
        if node == NIL:
            return

        # Parcours récursivement le sous-arbre gauche
        if node.left != NIL:
            self.inorder_walk(node=node.left)
        
        # Affiche la clé du nœud courant
        print(' ' + str(node.key), end='')

        # Parcours récursivement le sous-arbre droit
        if node.right != NIL:
            self.inorder_walk(node=node.right)

    def preorder_walk(self, node):
        """
        Parcours l'arbre en préordre (racine, gauche, droite) en commençant par un nœud donné.
        Affiche les clés sans les retourner.

        Args:
            node (Node ou int): Nœud à partir duquel commencer le parcours. Peut être NIL.
        """
        if node == NIL:
            return

        # Affiche la clé du nœud courant
        print(' ' + str(node.key), end='')

        # Parcours récursivement le sous-arbre gauche puis droit
        if node.left != NIL:
            self.preorder_walk(node=node.left)
        if node.right != NIL:
            self.preorder_walk(node=node.right)

    def show(self):
        """
        Affiche l'arbre sous forme de parcours en ordre croissant et en préordre sur deux lignes séparées.
        """
        self.inorder_walk(self.root)
        print()
        self.preorder_walk(self.root)
        print()

# Lecture du nombre de commandes
n = int(sys.stdin.readline())
T = Tree()

# Exécute n commandes issues de l'entrée standard
for i in range(n):
    line = sys.stdin.readline().split()
    
    if len(line) == 1:
        # Si la ligne ne contient qu'un mot-clé (ex : "print"), on affiche l'arbre
        T.show()
    else:
        # Sinon, on considère que c'est une commande d'insertion du style "insert X"
        key = int(line[1])
        T.insert(Node(key))