INF = 0x7fffffff  # Définition d'une constante INF représentant une très grande valeur entière (int max en 32 bits).
                   # Cette valeur sera utilisée pour initialiser les distances afin de signifier qu'elles sont 'infinies' ou non atteintes.

import heapq  # Importation du module heapq qui fournit une implémentation de tas binaire (heap) en Python,
              # utile pour manipuler des files de priorité efficaces dans l'algorithme de Dijkstra.

def dijkstra(V, to, start, goal):
    """
    Fonction implémentant l'algorithme de Dijkstra pour trouver le chemin le plus court dans un graphe.
    Paramètres :
    - V : nombre total de sommets dans le graphe.
    - to : liste d'adjacence où to[i] contient les arcs sortants depuis le sommet i sous forme (voisin, coût).
    - start : sommet de départ.
    - goal : sommet d'arrivée.
    Retour :
    - distance minimale entre start et goal.
    """

    dist = [INF] * V  # Création d'une liste 'dist' stockant la distance minimale trouvée à ce jour depuis start vers chaque sommet.
                      # Initialement, toutes les distances sont infinies car non calculées.
    Q = []            # Initialisation d'une liste Q qui servira de file de priorité (tas binaire) pour gérer les sommets à explorer.
    
    dist[start] = 0   # La distance du sommet de départ vers lui-même est de zéro car aucun déplacement n'est nécessaire.
    heapq.heappush(Q, (0, start))  # On insère dans la file de priorité un tuple (distance, noeud) pour le départ.
    
    while len(Q):  # Tant que la file de priorité n'est pas vide, on continue la recherche.
        t, s = heapq.heappop(Q)  # On extrait le sommet s avec la plus petite distance t actuellement connue.
        
        if s == goal:  # Si on a atteint le sommet d'arrivée, on peut interrompre la boucle car on a trouvé la distance minimale.
            break
        
        if dist[s] < t:  # Si la distance enregistrée dans dist est meilleure (plus petite) que t,
                         # cela signifie que ce sommet a déjà été traité avec un chemin plus court,
                         # on ignore donc la version actuelle.
            continue
        
        for i in to[s]:  # Pour chaque arc sortant depuis le sommet s,
            e, cost = i  # e est le noeud cible de l'arc, cost est le coût (distance) pour y aller.
            nt = t + cost # nt représente une nouvelle distance potentielle vers le noeud e via s.
            
            if dist[e] > nt:  # Si cette nouvelle distance nt est meilleure que celle précédemment connue pour e,
                dist[e] = nt  # on met à jour la distance minimale pour e.
                heapq.heappush(Q, (nt, e))  # et on ajoute e dans la file de priorité avec la nouvelle distance.
    
    return dist[goal]  # Une fois la boucle terminée (soit par rupture, soit après exploration complète), on retourne la distance minimale vers goal.



n = int(input()) + 1  # Lecture du nombre de noeuds, on ajoute 1 car l'indexation semble commencer à 1 (pas à 0).
                      # input() retourne une chaîne de caractères, int() la convertit en entier.

to = [[] for i in range(n)]  # Création d'une liste d'adjacence vide avec n sous-listes.
                             # Chaque sous-liste représente les arcs sortants d'un noeud i.

for i in range(int(input())):  # Lecture du nombre d'arcs (ou segments) du graphe.
    a, b, c, d = list(map(int, input().split(',')))  # Pour chaque arc, lecture de quatre entiers séparés par des virgules :
                                                     # a, b : sommets connectés par cet arc,
                                                     # c : coût dans une direction,
                                                     # d : coût dans l'autre direction.
    to[a].append((b, c))  # Ajout de l'arc dirigé de a vers b avec un coût c.
    to[b].append((a, d))  # Ajout de l'arc dirigé de b vers a avec un coût d.

s, g, V, P = list(map(int, input().split(',')))  # Lecture des paramètres supplémentaires :
                                                  # s : sommet de départ,
                                                  # g : sommet d'arrivée,
                                                  # V : une valeur initiale (probablement une récompense ou ressource),
                                                  # P : une pénalité ou un coût initial.

if s == g:  # Si le sommet de départ est le même que le sommet d'arrivée,
    print(V - P)  # alors on affiche juste la différence entre V et P, sans déplacement.
else:  # Sinon,
    # On calcule la différence entre V et P, puis on soustrait deux fois la distance de trajet total :
    # - dijkstra(n, to, s, g) : distance minimale de s vers g,
    # - dijkstra(n, to, g, s) : distance minimale de retour de g vers s.
    # On affiche le résultat final.
    print(V - P - dijkstra(n, to, s, g) - dijkstra(n, to, g, s))