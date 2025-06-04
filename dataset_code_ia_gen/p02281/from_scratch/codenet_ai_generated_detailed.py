# Définition de la classe Node pour représenter un noeud de l'arbre binaire
class Node:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left  # identifiant du fils gauche (-1 si aucun)
        self.right = right  # identifiant du fils droit (-1 si aucun)

# Fonction de parcours en préordre: racine, gauche, droite
def preorder(node_id, nodes, result):
    if node_id == -1:
        return
    result.append(node_id)              # visite la racine
    preorder(nodes[node_id].left, nodes, result)   # visite le sous-arbre gauche
    preorder(nodes[node_id].right, nodes, result)  # visite le sous-arbre droit

# Fonction de parcours en ordre: gauche, racine, droite
def inorder(node_id, nodes, result):
    if node_id == -1:
        return
    inorder(nodes[node_id].left, nodes, result)    # visite le sous-arbre gauche
    result.append(node_id)              # visite la racine
    inorder(nodes[node_id].right, nodes, result)   # visite le sous-arbre droit

# Fonction de parcours en postordre: gauche, droite, racine
def postorder(node_id, nodes, result):
    if node_id == -1:
        return
    postorder(nodes[node_id].left, nodes, result)  # visite le sous-arbre gauche
    postorder(nodes[node_id].right, nodes, result) # visite le sous-arbre droit
    result.append(node_id)              # visite la racine

def main():
    n = int(input())
    nodes = {}

    # Lecture des nodes, on stocke dans un dictionnaire id -> Node
    # Cela permet un accès direct par identifiant
    for _ in range(n):
        id, left, right = map(int, input().split())
        nodes[id] = Node(id, left, right)

    # Identifier la racine:
    # Tous les noeuds sauf la racine sont référencés comme enfant
    # On collecte les enfants et prend le noeud qui n'est enfant d'aucun autre
    children = set()
    for node in nodes.values():
        if node.left != -1:
            children.add(node.left)
        if node.right != -1:
            children.add(node.right)
    all_nodes = set(nodes.keys())
    root_candidates = all_nodes - children
    root = root_candidates.pop()  # il doit y avoir exactement 1 racine

    # Listes pour stocker les résultats
    pre_res = []
    in_res = []
    post_res = []

    # Exécute les traversées
    preorder(root, nodes, pre_res)
    inorder(root, nodes, in_res)
    postorder(root, nodes, post_res)

    # Affichage des résultats avec un espace avant chaque ID
    print("Preorder")
    print(' ' + ' '.join(map(str, pre_res)))
    print("Inorder")
    print(' ' + ' '.join(map(str, in_res)))
    print("Postorder")
    print(' ' + ' '.join(map(str, post_res)))

if __name__ == "__main__":
    main()