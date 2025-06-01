from operator import add  # Importation de la fonction 'add' du module 'operator', qui effectue l'addition de deux nombres.

# Définition d'une liste nommée 'pre' contenant des tuples.
# Chaque élément de 'pre' est un tuple de 3 tuples de 3 entiers chacun.
# Ces données semblent représenter des coûts ou des pré-calculs utilisés plus tard dans le code.
pre = [
    ((0, 1, 2), (1, 0, 1), (2, 1, 0)),  # premier tuple
    ((3, 2, 2), (2, 1, 1), (2, 1, 1)),  # deuxième tuple
    ((1, 1, 2), (1, 1, 2), (2, 2, 3)),  # troisième tuple
    ((3, 2, 2), (2, 2, 2), (2, 2, 3)),  # quatrième tuple
]

# Lecture d'un entier 'q' depuis l'entrée utilisateur.
# 'q' correspond au nombre de requêtes ou de cas de test à traiter.
q = int(input())

# Boucle qui s'exécute 'q' fois, avec une variable de boucle jetée '_',
# car la valeur de la variable d'itération n'est pas utilisée.
for _ in range(q):
    # Lecture d'un entier 'n' depuis l'entrée utilisateur.
    # 'n' semble représenter la moitié du nombre de livres ou une autre dimension.
    n = int(input())

    # Lecture d'une chaîne de caractères qui représente l'état d'une série de livres,
    # où chaque caractère indique si un certain livre est présent ('Y') ou absent.
    # La compréhension de liste crée une liste de booléens: True si caractère 'Y', sinon False.
    books = [c == 'Y' for c in input()]

    # On crée ensuite une nouvelle liste nommée 'books' qui commence par le tuple (0,0),
    # puis contient des tuples créés en associant deux éléments de la liste précédente:
    # 'books[:2 * n]' est la première moitié des livres, 'books[2 * n:]' la seconde moitié.
    # 'zip' fait correspondre ces deux listes élément par élément,
    # et 'list()' convertit l'itérateur résultant en liste.
    # Enfin, on ajoute un autre tuple (0,0) à la fin pour encapsuler la liste.
    books = [(0, 0)] + list(zip(books[:2 * n], books[2 * n:])) + [(0, 0)]

    # Création d'une liste 'shelves' où chaque élément est calculé à partir de deux tuples successifs de 'books'.
    # 'iter(books)' crée un itérateur sur 'books'.
    # '*[iter(books)] * 2' crée une liste contenant deux fois le même itérateur.
    # 'zip' groupera ainsi les éléments par paires successives (windowing).
    # Pour chaque paire ((u1, l1), (u2, l2)), on calcule:
    # bitwise OR entre u1 et u2 (opérateur '|') multiplié par 2, additionné avec bitwise OR entre l1 et l2.
    # Le résultat est un entier codant certaines informations issues des tuples.
    shelves = [(u1 | u2) * 2 + (l1 | l2) for (u1, l1), (u2, l2) in zip(*[iter(books)] * 2)]

    # Initialisation d'une liste 'ans' avec des valeurs [0, 1, 2].
    # Cette liste représente un état ou des coûts cumulés initialisés à ces valeurs.
    ans = [0, 1, 2]

    # Parcours de chaque valeur 'key' dans la liste 'shelves'.
    # Pour chaque clé, on va calculer une nouvelle liste 'new_ans'.
    for key in shelves:
        # Pour chaque tuple 'costs' dans pre[key], on effectue l'addition élément par élément
        # entre 'ans' et 'costs' (grâce à 'map(add, ans, costs)'), puis on prend le minimum de ces sommes.
        # 'new_ans' sera donc une liste de trois éléments représentant les nouveaux coûts minimaux.
        new_ans = [min(map(add, ans, costs)) for costs in pre[key]]

        # On remplace la liste 'ans' par la nouvelle liste calculée 'new_ans'.
        ans = new_ans

    # Finalement, on affiche la somme de ans[0] et de n.
    # ans[0] représente le coût minimal ou le résultat final ajusté par la valeur 'n'.
    print(ans[0] + n)