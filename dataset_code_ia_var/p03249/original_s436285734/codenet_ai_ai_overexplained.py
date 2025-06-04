import sys  # Importation du module système pour la gestion d'entrée/sortie et des fonctionnalités systèmes
input = sys.stdin.readline  # Redéfinition de la fonction input avec une lecture plus rapide de ligne pour les grands inputs

# Lecture d'un entier N depuis l'entrée standard et conversion en entier avec int
N = int(input())

# Création d'une liste D :
# Index 0 contient None car les sommets sont numérotés à partir de 1.
# Ensuite, on lit N entiers depuis l'entrée, un pour chaque sommet, et on les place dans la liste.
D = [None] + [int(input()) for _ in range(N)]

# Création d'une liste parent :
# parent[i] contiendra le parent du sommet i. On initialise par None. 
# On met N+1 éléments car les sommets sont de 1 à N inclus (on ignore l'indice 0).
parent = [None] * (N + 1)

# Création de la liste size :
# size[i] servira à garder la taille du sous-arbre (nombre de sommets dedans, lui-même inclus) pour le sommet i.
# On met None à l'indice 0 car on ne l'utilise pas.
# Pour chaque sommet de 1 à N, la taille initiale du sous-arbre est 1 (lui-même).
size = [None] + [1] * N

# Création d'un dictionnaire pour associer à chaque valeur d (stockée dans D) l'indice i correspondant.
# Utile pour retrouver l'indice d'un sommet à partir de sa valeur D[i].
d_to_i = {d: i for i, d in enumerate(D)}

# Création d'une liste D_desc :
# On trie les valeurs D[1:] (celles associées aux sommets, car D[0] est None) dans l'ordre décroissant.
D_desc = sorted(D[1:], reverse=True)

# Création d'une liste D_subtree :
# D_subtree[i] servira à accumuler la somme des tailles des sous-arbres des enfants du sommet i.
# On l'initialise à zéro pour tous les sommets (positions 0 à N).
D_subtree = [0] * (N + 1)

# Initialisation d'une liste qui stockera les arêtes du résultat sous forme de chaînes 'i p'
edges = []

# On suppose a priori que la construction va réussir, donc bl = True
bl = True

# Parcours des valeurs de D dans l'ordre décroissant, sauf la dernière valeur (le "root")
for d in D_desc[:-1]:
    # Recherche de l'indice i correspondant à la valeur d dans le dictionnaire
    i = d_to_i[d]
    # Calcul de la valeur attendue du parent de ce sommet i
    # d est la valeur D[i]
    # On enlève N (nombre total de sommets)
    # puis on ajoute deux fois la taille du sous-arbre courant
    # Ce calcul est spécifique à l'algorithme ici (ex : reconstruction d'un arbre depuis la taille de sous-arbre)
    d_parent = d - N + 2 * size[i]
    # Vérification si la valeur du parent existe bien dans d_to_i (sinon impossible de construire l'arbre)
    if d_parent not in d_to_i:
        # Si on ne trouve pas un parent valide, on arrête tout et on marque échec
        bl = False
        break
    # Trouve l'indice du parent
    p = d_to_i[d_parent]
    # On ajoute cette arête au résultat sous la forme 'i p'
    edges.append('{} {}'.format(i, p))
    # On note que le parent du sommet i est p
    parent[i] = p
    # On met à jour la taille du sous-arbre du parent p en rajoutant la taille du sous-arbre i
    size[p] += size[i]
    # On additionne aussi à D_subtree[p] la somme des tailles des sous-arbres en-dessous de i, plus la taille de i lui-même
    D_subtree[p] += D_subtree[i] + size[i]

# Le sommet racine doit être le sommet à la valeur D_desc[-1] (plus petite valeur restante après la boucle)
root = d_to_i[D_desc[-1]]

# On vérifie une condition supplémentaire pour valider que la reconstruction est correcte :
# La somme des sous-arbres de la racine doit être égale à la valeur D[root] attendue
bl &= (D_subtree[root] == D[root])

# Si tout s'est bien passé, on affiche chaque arête, chacune sur une ligne (ordre de la construction)
if bl:
    print('\n'.join(edges))
# Sinon il n'existait pas de telle construction possible, on affiche -1
else:
    print(-1)