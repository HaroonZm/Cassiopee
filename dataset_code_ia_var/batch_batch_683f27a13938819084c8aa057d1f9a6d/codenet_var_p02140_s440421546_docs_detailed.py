from collections import deque

def main():
    """
    Lecture des données d'entrée et calcul du plus court chemin et du nombre de chemins
    dans une grille, avec déplacements possibles sur les 4 directions et possibilité de 
    sauter instantanément vers les bords de la grille par 'téléportation'.
    A la fin, affiche la longueur du plus court chemin et le nombre de chemins modulo MOD.
    """

    # Lecture des paramètres d'entrée : dimensions de la grille et coordonnées des points
    R, C, ay, ax, by, bx = map(int, input().split())

    # Constantes pour le modulo et une valeur d'infini (pour initialiser les distances)
    MOD = INF = 10**9 + 7

    # Initialisation de la grille des distances avec INF et de la grille du nombre de chemins à 0
    dists = [[INF] * C for _ in range(R)]       # dists[y][x] = distance minimale pour (x,y)
    ptns = [[0] * C for _ in range(R)]          # ptns[y][x] = nombre de plus courts chemins pour (x,y)
    dists[ay][ax] = 0                           # Distance à la case de départ = 0
    ptns[ay][ax] = 1                            # Un seul chemin pour atteindre le départ

    # File de priorité: prend les cases à traiter, triées d'abord par la distance
    # (on note (distance courante, x, y))
    q = deque([(0, ax, ay)])

    # Déplacements possibles (droite, bas, gauche, haut)
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    # Variable pour stocker la longueur du plus court chemin jusqu'à l'arrivée
    ans_d = None

    while q:
        d, x, y = q.popleft()

        # Si on a déjà trouvé l'arrivée par le plus court chemin, on s'arrête si la distance augmente
        if ans_d is not None and d > ans_d:
            break

        # Si la position courante est la cible, on stocke la longueur du chemin correspondant
        if (x, y) == (bx, by):
            ans_d = d

        # Si on n'améliore pas la distance minimale à (x, y), on saute cette case
        if d > dists[y][x]:
            continue
        dists[y][x] = d

        # Exploration des cases adjacentes (haut, bas, gauche, droite)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # Vérification que la case voisine reste dans la grille
            if not (0 <= nx < C) or not (0 <= ny < R):
                continue

            # Si la distance calculée n'améliore pas, on continue
            if d + 1 > dists[ny][nx]:
                continue

            # Si c'est la première visite, on l'ajoute à la file pour exploration prochaine
            if dists[ny][nx] == INF:
                q.append((d + 1, nx, ny))
                dists[ny][nx] = d + 1

            # Ajout du nombre de chemins de (x,y) vers la case voisine
            ptns[ny][nx] += ptns[y][x]
            ptns[ny][nx] %= MOD

        # Exploration de la 'téléportation' sur les bords (lignes et colonnes extrêmes)
        for nx, ny in ((x, 0), (x, R - 1), (0, y), (C - 1, y)):
            if d + 1 > dists[ny][nx]:
                continue
            if dists[ny][nx] == INF:
                q.append((d + 1, nx, ny))
                dists[ny][nx] = d + 1

            ptns[ny][nx] += ptns[y][x]
            ptns[ny][nx] %= MOD

    # Affichage du résultat : longueur du plus court chemin et nombre de plus courts chemins
    print(ans_d, ptns[by][bx] % MOD)

if __name__ == "__main__":
    main()