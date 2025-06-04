# Importation des fonctions heappop et heappush depuis le module heapq
# Le module heapq fournit une implémentation du tas binaire (heap) pour Python
from heapq import heappop, heappush

# Lecture de deux entiers à partir de la ligne d'entrée standard.
# input() lit une ligne de texte depuis l'entrée, split() sépare la ligne par les espaces,
# map(int, ...) convertit chaque morceau en entier.
# Le résultat est unpacké dans les variables n et q.
# n : nombre de files de priorité (priority queues)
# q : nombre d'opérations à traiter
n, q = map(int, input().split())

# Création d'une liste contenant n sous-listes vides.
# Chaque sous-liste représentera une file de priorité indépendante.
# La compréhension de liste [[] for _ in range(n)] crée n listes vides dans une liste principale.
pq = [[] for _ in range(n)]

# Boucle qui s'exécute q fois pour traiter chaque opération.
for _ in range(q):
    # Lecture d'une ligne à partir de l'entrée.
    # input() lit la ligne de commande/de requête de l'utilisateur.
    # ' 1' est concaténé à la chaîne lue pour garantir qu'il y aura au moins 3 éléments après split(),
    # même si l'entrée ne contient que 2 éléments.
    # split() sépare la ligne en parties distinctes (par défaut, séparées par des espaces).
    # [:3] permet de ne conserver que les 3 premiers éléments (op, t, x)
    # Ceci évite une erreur d'index dans les cas où l'entrée ne fournit pas x (pour les cas op="1" ou "2")
    op, t, x = (input() + ' 1').split()[:3]

    # Si l'opération demandée par l'utilisateur est '0' --> Insertion dans la file de priorité
    if op == '0':
        # heappush insère un nouvel élément dans la file de priorité.
        # Ici, int(t) convertit l'identifiant de la file en entier.
        # int(x) convertit la valeur à insérer en entier.
        # La multiplication par -1 permet d'utiliser le min-heap de heapq comme un max-heap,
        # car heapq ne gère que les minimums par défaut.
        # Ainsi, les entiers sont stockés négatifs pour obtenir un comportement de max-heap.
        heappush(pq[int(t)], int(x)*-1)
    # Si l'opération est '1' --> Afficher la valeur maximale de la file (sans la retirer)
    elif op == '1':
        # On vérifie si la file de priorité correspondante (pq[int(t)]) n'est pas vide.
        # Une liste vide correspond à une file vide ; la condition est donc False si la file est vide.
        if pq[int(t)]:
            # Affichage du premier élément de la file (l'élément max à cause du max-heap simulé).
            # pq[int(t)][0] donne la plus grande valeur (enregistrée sous forme négative).
            # On multiplie par -1 pour retrouver la valeur originale avant de l'afficher.
            print(pq[int(t)][0]*-1)
    # Sinon, c'est l'opération '2' --> Supprimer la valeur maximale de la file (pop du max)
    else:
        # Vérification que la file n'est pas vide pour éviter une erreur lors du retrait.
        if pq[int(t)]:
            # Suppression de l'élément ayant la priorité la plus haute (le plus grand en valeur)
            # heappop retire et retourne la plus petite valeur du heap (ici, c'est la plus grande
            # valeur originale à cause du stockage négatif)
            heappop(pq[int(t)])