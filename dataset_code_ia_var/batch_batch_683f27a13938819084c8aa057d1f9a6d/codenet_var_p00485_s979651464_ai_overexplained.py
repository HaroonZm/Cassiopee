from heapq import heappop as pop
from heapq import heappush as push

def solve():
    # Définition d'une valeur constante pour l'infini, utilisée pour initialiser les distances.
    # Ici, 10 puissance 18 est une très grande valeur qui agit comme "infini" dans le contexte de ce problème.
    INF = 10 ** 18

    # Définition de la classe "edge" représentant une arête du graphe.
    # Cette classe possède deux attributs :
    #   - to : l'indice du sommet de destination de l'arête.
    #   - cost : le coût (ou poids) associé à cette arête.
    class edge:
        def __init__(self, to, cost):
            self.to = to    # affecte le sommet de destination
            self.cost = cost  # affecte le coût de l'arête

    # Lecture des trois premiers entiers de l'entrée standard :
    #   - N : nombre de sommets dans le graphe
    #   - M : nombre d'arêtes dans le graphe
    #   - K : nombre de sommets initiaux pour l'algorithme de Dijkstra
    N, M, K = map(int, input().split())

    # Initialisation du graphe G comme une liste de listes.
    # G[i] contiendra la liste des arêtes sortantes du sommet i.
    # Chaque arête sera un objet de type "edge".
    G = [[] for i in range(N)]

    # Initialisation de la liste des distances d.
    # d[i] représentera la plus courte distance trouvée depuis le(s) sommet(s) de départ jusqu'au sommet i.
    # On remplit la liste avec la valeur INF pour signifier que les distances sont initialement infinies.
    d = [INF for i in range(N)]

    # Définition de la fonction dijkstra prenant en paramètre une liste lst de sommets sources.
    # Cette version permet de lancer Dijkstra à partir de plusieurs sources simultanément,
    # ce qui va trouver la plus courte distance depuis n'importe quelle source de lst jusqu'à chaque sommet.
    def dijkstra(lst):
        # Initialisation d'une file de priorité vide (version binaire du tas).
        que = []
        # Pour chaque sommet s dans la liste de sources :
        for s in lst:
            d[s] = 0  # La distance du sommet source à lui-même est toujours 0
            push(que, (0, s))  # On insère un tuple (distance, sommet) dans le tas de priorité

        # Boucle principale de l'algorithme :
        # On continue tant qu'il reste des sommets dans la file de priorité
        while len(que):
            # On extrait le sommet ayant actuellement la plus petite distance estimée
            p = pop(que) # p est un tuple (distance cumulée depuis la source, indice du sommet)
            v = p[1]     # v reçoit l'indice du sommet extrait
            # Si une distance plus courte a déjà été trouvée pour ce sommet, on continue vers le suivant
            if d[v] < p[0]:
                continue
            # On parcourt maintenant toutes les arêtes sortantes du sommet courant v
            for i in range(len(G[v])):
                e = G[v][i]  # e est une arête de type "edge"
                # Si une distance plus courte jusqu'à e.to (sommet destination) est trouvée via v
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # On met à jour la distance la plus courte
                    # On insère ce sommet dans la file de priorité pour exploration future
                    push(que, (d[e.to], e.to))

    # Lecture de chaque arête
    for i in range(M):
        # Pour chaque arête, on lit trois entiers :
        #   - s : sommet origine (1-indexé dans l'entrée)
        #   - t : sommet destination (1-indexé dans l'entrée)
        #   - c : coût de l'arête
        s, t, c = map(int, input().split())
        s -= 1  # on ajuste de l'indexation 1 vers 0 (python utilise 0-indexé)
        t -= 1
        # On ajoute l'arête dans les deux sens (graph non orienté)
        G[s].append(edge(t, c))  # arête allant de s à t avec coût c
        G[t].append(edge(s, c))  # arête allant de t à s avec coût c

    # Lecture des K sommets sources, qui sont également 1-indexés dans l'entrée
    # On les stocke dans la liste lst, en les convertissant en 0-indexé
    lst = [int(input()) - 1 for i in range(K)]

    # Lancement de l'algorithme de Dijkstra à partir des K sources de lst
    dijkstra(lst)

    # Initialisation d'une liste vide anss pour stocker les résultats intermédiaires
    anss = []
    # Pour accélérer l'append, on récupère la méthode append et on la stocke localement
    append = anss.append

    # Double boucle pour parcourir chaque sommet et chaque arête sortante de ce sommet
    for i in range(N):
        for e in G[i]:
            # On calcule x tel que :
            #   x = distance du sommet i depuis une source + distance du sommet destination e.to depuis une source + coût de l'arête
            x = d[i] + d[e.to] + e.cost
            # On souhaite prendre la valeur entière de x divisé par 2 et arrondie à l'entier supérieur si x est impair,
            # sinon arrondie à l'entier inférieur si x est pair.
            # Cette opération est équivalente à : (x + 1) // 2 pour x impair, x // 2 pour x pair.
            if x % 2:
                # Si x est impair, on ajoute 1 avant de diviser pour simuler un arrondi supérieur
                append(x // 2 + 1)
            else:
                # Si x est pair, une division entière suffit
                append(x // 2)

    # On affiche la valeur maximale parmi toutes celles stockées dans la liste anss
    print(max(anss))

# Appel de la fonction principale pour exécuter le programme
solve()