# Solution complète en Python pour le problème "パケット転送" avec commentaires détaillés

from collections import deque

def main():
    n = int(input())  # Nombre total de routeurs
    graph = dict()

    # Lecture des informations de connexion pour chaque routeur
    for _ in range(n):
        data = input().split()
        r = int(data[0])  # Numéro du routeur
        k = int(data[1])  # Nombre de routeurs directement connectés
        connected = list(map(int, data[2:2+k]))  # Liste des routeurs connectés
        graph[r] = connected

    p = int(input())  # Nombre de paquets à traiter

    # Pour chaque paquet, on effectue une recherche en largeur (BFS) pour trouver
    # le plus petit nombre possible de routeurs à traverser jusqu'à destination
    for _ in range(p):
        s, d, v = map(int, input().split())  # source, destination, TTL

        # Si source == destination n'arrive pas selon l'énoncé
        # On doit déterminer le chemin le plus court (en nombre de routeurs traversés),
        # avec comme contrainte que le TTL minimum nécessaire est le nombre de routeurs sur le chemin.

        # BFS pour trouver le chemin le plus court
        # On stocke les distances (nombre de routeurs traversés) depuis s
        dist = {node: None for node in graph}
        dist[s] = 1  # compter le routeur source comme premier routeur

        queue = deque([s])

        while queue:
            current = queue.popleft()
            # On ne décrémente pas le TTL ici mais on vérifiera après BFS car TTL est comparé avec la distance
            if current == d:
                break
            for nxt in graph.get(current, []):
                if dist[nxt] is None:
                    dist[nxt] = dist[current] + 1
                    queue.append(nxt)

        # dist[d] contient le nombre minimal de routeurs parcourus si on a trouvé un chemin
        # Sinon dist[d] est None

        # Selon l'énoncé: La TTL est décrémentée à chaque routeur sauf au dernier (destination)
        # Donc le TTL minimum nécessaire = dist[d] - 1 (car on ne décrémente pas TTL au d)
        # Mais dist compte la source comme 1, donc nombre de routeurs traversés c'est dist[d].
        # Ex: chemin 6->1->5 est dist=3, TTL minimum = 2 (6 et 1) donc v >= dist[d] - 1

        if dist[d] is None:
            print("NA")
        else:
            needed = dist[d] - 1
            if v >= needed:
                print(dist[d])
            else:
                print("NA")

if __name__ == "__main__":
    main()