import sys  # Importe le module sys qui permet d'accéder à certaines fonctionnalités du système, comme les flux d'entrée/sortie
from heapq import heappush, heappop  # Importe les fonctions heappush et heappop du module heapq, permettant de gérer des files de priorité (tas binaire)
readline = sys.stdin.buffer.readline  # Définit readline comme une fonction pour lire une ligne depuis l'entrée standard, en mode binaire pour plus d'efficacité
write = sys.stdout.write  # Définit write comme une fonction pour écrire une chaîne de caractères sur la sortie standard

def solve():  # Définit une fonction nommée solve qui va résoudre un sous-problème à chaque appel
    # Lecture de trois entiers séparés par des espaces. Ils correspondent au nombre de sommets (N),
    # au nombre d'arêtes (M) et au coût maximal permis (C).
    N, M, C = map(int, readline().split())
    # Vérifie si tous les paramètres valent 0, ce qui est ici une condition d'arrêt pour la boucle principale.
    if N == M == C == 0:
        return False  # Indique qu'il faut arrêter d'appeler la fonction solve

    # Création d'une liste d'adjacence vide pour chaque sommet du graphe.
    # Au départ, le graphe G est une liste de N listes vides.
    G = [[] for i in range(N)]

    # Boucle pour lire les M arêtes du graphe
    for i in range(M):
        # Lecture d'une arête: f (départ), t (arrivée), c (coût)
        f, t, c = map(int, readline().split())
        f -= 1  # Décalage pour utiliser des indices en base 0 au lieu de base 1 (Python utilise base 0)
        t -= 1  # Même chose pour le sommet d'arrivée
        G[f].append((t, c))  # Ajoute un couple (sommet d'arrivée, coût) à la liste de f

    INF = 10**18  # Définit une valeur "infinie" qui sera utilisée pour initialiser les distances
    # Création de la table des distances :
    # dist[v][k] représente la plus courte distance (coût minimal) pour atteindre le sommet v
    # en ayant effectué exactement k utilisations d'une "remise" ou "carte spéciale" (voir logique du problème)
    # La taille est dist[N][N+1] pour permettre jusqu'à N usages (pour chaque sommet)
    dist = [[INF]*(N+1) for i in range(N)]

    # Initialisation de la file de priorité (le "tas"), utilisée pour faire une variante de Dijkstra
    # L'élément du tas est un triplet (coût cumulé, sommet courant, nombre de remises utilisées)
    que = [(0, 0, 0)]  # Commence du sommet 0 avec 0 coût et 0 "remises"
    dist[0][0] = 0  # La distance pour arriver au sommet 0 sans remise utilisée est 0

    # Boucle principale de l'algorithme de Dijkstra
    while que:
        # Prend l'élément ayant le plus petit coût courant (priority queue - file de priorité)
        cost, v, k = heappop(que)
        # Si une meilleure distance a déjà été trouvée pour ce même sommet et "nombre de remises", on saute
        if dist[v][k] < cost:
            continue
        # Parcours de tous les voisins w du sommet courant v,
        # d est le coût de l'arête de v vers w
        for w, d in G[v]:
            # Cas 1 : on "paye" l'arête normalement (pas d'utilisation de remise)
            if cost + d < dist[w][k]:
                # Si le chemin actuel améliore le coût pour aller à w sans utiliser de remise supplémentaire
                dist[w][k] = cost + d  # On met à jour la meilleure distance trouvée
                # On ajoute ce nouvel état dans la file de priorité
                heappush(que, (cost + d, w, k))

            # Cas 2 : on utilise une remise (si autorisé, c'est-à-dire k < N)
            # La remise permet de traverser l'arête sans payer son coût (cost ne bouge pas)
            if k < N and cost < dist[w][k+1]:
                # Si l'utilisation d'une remise améliore la situation pour w en ayant utilisé une remise de plus
                dist[w][k+1] = cost  # On met à jour la distance correspondante
                # On ajoute ce nouvel état dans la file de priorité
                heappush(que, (cost, w, k+1))

    # On cherche maintenant le plus petit nombre de remises qu'il faut utiliser pour atteindre le sommet final
    for k in range(N+1):  # On teste pour chaque nombre de remises, de 0 à N inclus
        # Si la meilleure distance pour atteindre le sommet de fin (N-1) en utilisant k remises
        # ne dépasse pas le coût maximal autorisé (C)
        if dist[N-1][k] <= C:
            # On écrit le nombre minimal de remises nécessaires suivi d'un retour à la ligne
            write("%d\n" % k)
            break  # On s'arrête dès qu'on a trouvé la solution optimale
    return True  # Indique à la boucle principale de continuer à appeler solve pour la prochaine instance

# Boucle principale : appelle solve() tant que solve() retourne True.
# Dès que solve() retourne False (ce qui signifie N == M == C == 0), la boucle s'arrête.
while solve():
    ...  # Utilise l'ellipse comme "no-op" (aucune instruction) - c'est simplement un placeholder pour respecter la syntaxe Python