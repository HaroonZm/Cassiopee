# Importation de la fonction add du module operator.
# Cette fonction permet d'additionner deux éléments.
from operator import add

# Définition de la liste 'pre'. C'est une liste de 4 éléments,
# chaque élément est un tuple de 3 tuples.
# Chaque tuple interne contient 3 entiers.
# Ces valeurs serviront à déterminer les coûts lors de l'algorithme,
# en fonction de la valeur de la variable 'key'.
pre = [
    # Premier élément pour key == 0
    ((0, 1, 2), (1, 0, 1), (2, 1, 0)),
    # Deuxième élément pour key == 1
    ((3, 2, 2), (2, 1, 1), (2, 1, 1)),
    # Troisième élément pour key == 2
    ((1, 1, 2), (1, 1, 2), (2, 2, 3)),
    # Quatrième élément pour key == 3
    ((3, 2, 2), (2, 2, 2), (2, 2, 3)),
]

# Lecture d'un entier à partir de l'entrée utilisateur, converti en int.
# Cette variable 'q' représente le nombre de cas de tests à traiter.
q = int(input())

# Boucle for qui s'exécutera 'q' fois (autant de cas de tests qu'indiqué par l'utilisateur).
for _ in range(q):
    # Lecture de l'entier 'n' depuis l'entrée utilisateur.
    # Cet entier représente une dimension ou une taille utilisée plus tard.
    n = int(input())
    
    # Lecture d'une chaîne de caractères depuis l'entrée utilisateur.
    # Chaque caractère de la chaîne est comparé à 'Y' (pour Yes),
    # afin de générer une liste de booléens:
    # True si le caractère est 'Y', False sinon.
    books = [c == 'Y' for c in input()]
    
    # On prépare une nouvelle liste 'books' de tuples.
    # Explications détaillées:
    # - On ajoute d'abord le tuple (0, 0) au début. Ceci sert de bordure (padding) gauche.
    # - Ensuite, on crée une liste de tuples par paires en combinant:
    #   -> les 2*n premiers booléens (books[:2 * n]) [liste du haut],
    #   -> et les 2*n ceux d'après (books[2 * n:]) [liste du bas].
    #   Ceci avec la fonction zip, qui crée un tuple pour chaque couple de l'itérateur.
    # - On ajoute de nouveau le tuple (0, 0) à la fin, servant de bordure droite.
    #
    # Le résultat est une liste dont le premier et dernier élément sont (0, 0),
    # et les éléments du milieu sont des tuples représentant l'état de livres
    # sur deux étagères (haut et bas), pour chaque colonne.
    books = [(0, 0)] + list(zip(books[:2 * n], books[2 * n:])) + [(0, 0)]
    
    # Création de la liste 'shelves' qui représentera l'état combiné des livres
    # sur deux colonnes adjacentes (i et i+1), transformé en un nombre de 0 à 3.
    # Explications détaillées:
    # - On itère simultanément sur books par paires de deux (zip sur [iter(books)] * 2).
    #   Cela permet d'obtenir (u1, l1) et (u2, l2): l'état du haut/gauche puis du haut/droite,
    #   et du bas/gauche puis du bas/droite, respectivement.
    # - Pour chaque paire, on applique l'opérateur logique 'ou' (|) sur le haut et le bas,
    #   puis on calcule (u1 | u2) * 2 + (l1 | l2), ce qui produit une valeur dans [0, 3].
    shelves = [(u1 | u2) * 2 + (l1 | l2) for (u1, l1), (u2, l2) in zip(*[iter(books)] * 2)]
    
    # Initialisation de la liste 'ans' à [0, 1, 2].
    # Cette liste gardera, pour chaque option, le coût minimal courant.
    ans = [0, 1, 2]
    
    # Boucle sur chaque valeur de 'key' dans la liste 'shelves'.
    # Pour chaque colonne, la valeur 'key' détermine le coût à ajouter selon 'pre'.
    for key in shelves:
        # Pour chaque ensemble de coûts 'costs' parmi les 3 disponibles dans pre[key],
        # on calcule l'addition élément par élément (add) de ans et costs,
        # puis on prend le minimum des résultats (min(map(add, ans, costs))).
        # Ceci donne le meilleur coût possible pour chaque option, stocké dans new_ans.
        new_ans = [min(map(add, ans, costs)) for costs in pre[key]]
        
        # On met à jour ans avec le nouveau tableau de coût optimal.
        ans = new_ans
    
    # Affichage sur la sortie standard de la valeur finale,
    # qui est le coût minimal trouvé (ans[0]) additionné à n.
    print(ans[0] + n)