import sys

def solve():
    # Lire la première ligne pour obtenir N et K
    input_lines = sys.stdin.readlines()
    first_line = input_lines[0].strip()
    N, K = map(int, first_line.split())

    # Créer une liste de 10 sous-listes pour les genres
    G = []
    for i in range(10):
        G.append([])

    # Lire chaque ligne suivante pour récupérer les prix et genres
    for line in input_lines[1:]:
        c, g = map(int, line.strip().split())
        G[g - 1].append(c)

    # Pour chaque genre, trier les prix dans l'ordre décroissant
    # puis calculer des prix cumulés ajustés
    for genre in G:
        genre.sort(reverse=True)
        for i in range(1, len(genre)):
            genre[i] = genre[i] + genre[i-1] + 2 * i

    # Initialiser la liste C avec des zéros
    C = [0] * (K + 1)

    # Mettre à jour C en considérant les différentes combinaisons de prix
    for genre in G:
        pre_C = C[:]
        length = len(genre)
        for n in range(length, 0, -1):
            p = genre[n-1]
            for i in range(len(C) - n + 1):
                v1 = pre_C[i + n] + p
                v2 = C[i]
                if v1 > v2:
                    C[i] = v1

    # Afficher le résultat final
    print(C[0])

solve()