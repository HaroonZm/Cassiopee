import sys
from collections import deque

# Fonction principale qui gère la lecture de plusieurs jeux de données
def main():
    input = sys.stdin.readline
    while True:
        # Lecture des dimensions de la grille : n (largeur), m (hauteur)
        line = input().strip()
        if not line:
            break
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            # Fin des données d'entrée
            break

        # Lecture de la grille
        maze = [list(input().strip()) for _ in range(m)]

        # Résoudre pour ce jeu de données et afficher le résultat
        print(min_climb_count(n, m, maze))


def min_climb_count(n, m, maze):
    """
    Calcule le nombre minimum de fois que le ninja doit sortir du douve (# -> . ou # -> &)
    pour aller depuis l'extérieur (quelque part en dehors des bords non douve) jusqu'au donjon (&).

    Approche :
    - On considère qu'on peut commencer en tout point accessible sur les bords où on n'est pas déjà dans un douve (#).
      En effet, le ninja commence hors du château, donc sur les bordures non dunkes.
    - On fait une BFS modifiée sur la grille où chaque position est notée avec le nombre minimal de "sorties de douve" utilisées pour y arriver.
    - On modélise les transitions à coût 0 ou 1:
      * se déplacer dans le douve (#) ne coûte rien (pas besoin de sortir puisqu'on nage dans le douve),
      * sortir de douve vers une case sèche ('.' ou '&') coûte 1 (car on doit grimper hors du douve).
      * se déplacer sur des cases sèches ('.' ou '&') coûte 0 (rien à faire)
    - L'algorithme utilise une deque pour effectuer un 0-1 BFS (un BFS pondéré avec poids 0 ou 1)
      pour obtenir le coût minimal (nombre de sorties de douve).
    - Le résultat est le coût minimal pour atteindre le '&'.

    Paramètres:
    n (int): largeur
    m (int): hauteur
    maze (List[List[str]]): grille

    Retour:
    int: nombre minimal de sorties de douve
    """

    # Directions possibles (N, S, E, O)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Trouver la position du donjon (&)
    goal = None
    for y in range(m):
        for x in range(n):
            if maze[y][x] == '&':
                goal = (x, y)
                break
        if goal is not None:
            break

    # distance[x][y] : nombre minimal de sorties du douve pour atteindre (x,y)
    # On initialise à une grande valeur
    INF = 10**9
    dist = [[INF] * n for _ in range(m)]

    # Initialisation de la deque pour 0-1 BFS
    dq = deque()

    # On considère toutes les positions "dehors", c'est-à-dire les cases sur les bords
    # qui ne sont pas dans des douves (#). Le ninja commence ici à coût 0.
    # Intuition: on est en dehors et on peut entrer dans le château en partant de ces cases.
    for y in [0, m-1]:
        for x in range(n):
            if maze[y][x] != '#':
                dist[y][x] = 0
                dq.appendleft((x, y))
    for y in range(1, m-1):
        for x in [0, n-1]:
            if maze[y][x] != '#':
                dist[y][x] = 0
                dq.appendleft((x, y))

    # 0-1 BFS
    while dq:
        x, y = dq.popleft()

        # Arrivé au donjon
        if (x, y) == goal:
            return dist[y][x]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # Passage du type de terrain :
                # Savoir si on change de zone :
                # de douve '#' vers non douve '.' ou '&' => +1 coût (grimpe)
                # sinon 0 coût
                current = maze[y][x]
                nxt = maze[ny][nx]

                # Calcul du coût du mouvement
                # Si on va dans un douve, pas de coût supplémentaire
                # Si on sort d'un douve vers un non-douve, coût = 1
                # Si on est dans non douve et reste dans non douve, coût = 0
                cost = dist[y][x]  # coût actuel

                if current == '#' and nxt != '#':
                    # grimper hors du douve => on paye 1
                    cost += 1
                # sinon cost même

                # Mettre à jour si coûts meilleurs
                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    # si le coût n'a pas augmenté, on met devant (priorité)
                    if (current == '#' and nxt != '#'):
                        # coût augmenté d'un => mettre en queue
                        dq.append((nx, ny))
                    else:
                        # pas de coût => priorité => mettre devant
                        dq.appendleft((nx, ny))

    # Si on ne peut pas atteindre le donjon, retourner 0 (problème ne l'indique pas, c'est une hypothèse)
    return 0

if __name__ == "__main__":
    main()