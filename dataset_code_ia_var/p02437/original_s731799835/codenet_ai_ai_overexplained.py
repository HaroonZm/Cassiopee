# Importation du module 'sys' pour accéder à certains objets et fonctions système
import sys

# Redéfinition de la fonction 'input' afin de lire plus rapidement les entrées standard grâce à 'sys.stdin.readline'
input = sys.stdin.readline

# Importation du module 'heapq', qui contient des fonctions pour manipuler des tas (heaps),
# c'est-à-dire des structures de données permettant d'extraire facilement le minimum ou le maximum
import heapq

# Lecture et séparation des deux premiers entiers de la première ligne d'entrée
# 'N' : nombre de tas (heaps) à gérer
# 'Q' : nombre de requêtes (queries) à traiter
N, Q = map(int, input().split())

# Création d'une liste de N listes vides.
# Chaque sous-liste représente un tas (heap) distinct associé à un indice de 0 à N-1
H = [[] for _ in range(N)]

# Boucle qui s'exécute Q fois, c'est-à-dire une fois par requête
for _ in range(Q):
    # Lecture de la prochaine ligne d'entrée, conversion de chaque élément en entier, et stockage dans la liste 'q'
    # Les requêtes peuvent avoir différentes longueurs (2 ou 3 éléments) selon l'opération à effectuer
    q = list(map(int, input().split()))
    
    # Si le premier élément de la requête (q[0]) vaut 0, il s'agit d'une opération d'insertion
    if q[0] == 0:
        # 'q[1]' : indice du tas (heap) dans lequel ajouter la valeur
        # 'q[2]' : valeur à insérer dans le tas
        # On utilise 'heappush' pour insérer l'élément dans le tas tout en maintenant la propriété de structure du heap
        # On insère '-q[2]' au lieu de 'q[2]' car 'heapq' implémente un tas binaire min, 
        # et on souhaite ici simuler un tas max (le plus grand en haut) en inversant les signes
        heapq.heappush(H[q[1]], -q[2])
    
    # Si le premier élément de la requête (q[0]) vaut 1, il s'agit d'une opération de consultation (peek)
    elif q[0] == 1:
        # On vérifie d'abord si le tas à l'indice 'q[1]' n'est pas vide
        if H[q[1]]:
            # On accède au premier élément du tas avec H[q[1]][0]
            # Comme on a stocké les valeurs négatives, on remet le signe positif avec '-'
            # On affiche la valeur la plus grande contenue dans le tas sans la retirer
            print(-H[q[1]][0])
    
    # Si le premier élément de la requête (q[0]) n'est ni 0 ni 1 (donc 2), il s'agit d'une opération de suppression
    else:
        # On vérifie si le tas à l'indice 'q[1]' n'est pas vide
        if H[q[1]]:
            # On retire et ignore l'élément le plus grand du tas à l'aide de 'heappop'
            # 'heappop' enlève le plus petit élément en valeur (ici, le plus négatif, donc le maximum d'origine)
            heapq.heappop(H[q[1]])