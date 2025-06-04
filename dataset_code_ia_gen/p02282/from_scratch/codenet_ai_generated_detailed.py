# Lecture des entrées
n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

# Fonction récursive pour reconstruire l'arbre et imprimer le postordre
def postorder_from_pre_in(preorder, inorder):
    # Si la liste est vide, retourner une liste vide
    if not preorder:
        return []

    # Le premier élément du préordre est la racine
    root = preorder[0]

    # Trouver la position de la racine dans l'inordre
    root_index_in_inorder = inorder.index(root)

    # Séparer l'inordre en sous-arbres gauche et droit
    left_inorder = inorder[:root_index_in_inorder]
    right_inorder = inorder[root_index_in_inorder+1:]

    # En fonction de la taille du sous-arbre gauche, séparer le préordre
    left_preorder = preorder[1:1+len(left_inorder)]
    right_preorder = preorder[1+len(left_inorder):]

    # Appels récursifs pour sous-arbres gauche et droit
    left_postorder = postorder_from_pre_in(left_preorder, left_inorder)
    right_postorder = postorder_from_pre_in(right_preorder, right_inorder)

    # La postordre est : sous-arbre gauche + sous-arbre droit + racine
    return left_postorder + right_postorder + [root]

# Calcul du postordre
postorder = postorder_from_pre_in(preorder, inorder)

# Impression du résultat
print(' '.join(map(str, postorder)))