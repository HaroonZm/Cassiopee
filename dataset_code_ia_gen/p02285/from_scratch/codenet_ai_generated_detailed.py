import sys
sys.setrecursionlimit(10**7)

# Classe représentant un noeud dans l'arbre binaire de recherche
class Node:
    def __init__(self, key):
        self.key = key  # clé du noeud
        self.parent = None  # référence au parent
        self.left = None  # référence au fils gauche
        self.right = None  # référence au fils droit

# Classe représentant l'arbre binaire de recherche (BST)
class BST:
    def __init__(self):
        self.root = None  # racine de l'arbre initialement vide

    # Fonction utilitaire pour insérer récursivement une clé dans l'arbre
    def __insert(self, root, node):
        if root is None:
            return node
        if node.key < root.key:
            root.left = self.__insert(root.left, node)
            root.left.parent = root
        else:
            root.right = self.__insert(root.right, node)
            root.right.parent = root
        return root

    # Insère une clé donnée dans l'arbre BST
    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            self.root = self.__insert(self.root, node)

    # Recherche un noeud par clé dans l'arbre
    def find(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    # Parcours infixe (inorder) récursif qui liste les clés dans l'ordre croissant
    def inorder_walk(self, node, res):
        if node is not None:
            self.inorder_walk(node.left, res)
            res.append(node.key)
            self.inorder_walk(node.right, res)

    # Parcours préfixe (preorder) récursif qui liste les clés selon ordre préfixe
    def preorder_walk(self, node, res):
        if node is not None:
            res.append(node.key)
            self.preorder_walk(node.left, res)
            self.preorder_walk(node.right, res)

    # Trouve le noeud minimal d'un sous-arbre donné
    def tree_minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Fonction utilitaire qui remplace le sous-arbre racine u par le sous-arbre racine v
    def __transplant(self, u, v):
        if u.parent is None:
            self.root = v  # u est racine, on remplace la racine par v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    # Supprime un noeud z donné selon l'algorithme présenté
    def delete(self, key):
        z = self.find(key)
        if z is None:
            return  # la clé n'existe pas dans l'arbre, rien à faire
        # Cas 1 : z n'a pas d'enfant
        if z.left is None and z.right is None:
            self.__transplant(z, None)
        # Cas 2 : z a un seul enfant à droite
        elif z.left is None:
            self.__transplant(z, z.right)
        # Cas 2 : z a un seul enfant à gauche
        elif z.right is None:
            self.__transplant(z, z.left)
        # Cas 3 : z a deux enfants
        else:
            y = self.tree_minimum(z.right)  # successeur de z
            if y.parent != z:
                # On enlève y de son endroit, on attache y.right au parent de y
                self.__transplant(y, y.right)
                # On fait pointer le sous-arbre droit de z à y.right
                y.right = z.right
                y.right.parent = y
            # On remplace z par y
            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y

def main():
    import sys
    input = sys.stdin.readline

    m = int(input())
    bst = BST()
    for _ in range(m):
        line = input().strip()
        if line.startswith("insert"):
            _, k = line.split()
            k = int(k)
            bst.insert(k)
        elif line.startswith("find"):
            _, k = line.split()
            k = int(k)
            node = bst.find(k)
            if node is not None:
                print("yes")
            else:
                print("no")
        elif line.startswith("delete"):
            _, k = line.split()
            k = int(k)
            bst.delete(k)
        elif line == "print":
            inorder_res = []
            preorder_res = []
            bst.inorder_walk(bst.root, inorder_res)
            bst.preorder_walk(bst.root, preorder_res)
            print(" " + " ".join(map(str, inorder_res)))
            print(" " + " ".join(map(str, preorder_res)))

if __name__ == "__main__":
    main()