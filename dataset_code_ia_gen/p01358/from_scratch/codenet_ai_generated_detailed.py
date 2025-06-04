import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    # Lecture des paramètres
    n, u, v, m = map(int, input().split())
    # u,v sont les conditions de victoires : nombre minimum de lignes alignées

    # Lecture des matrices de nombres écrits par Usagi et Neko
    # Matrice Usagi, taille n x n
    usagi_nums = [list(map(int, input().split())) for _ in range(n)]
    # Matrice Neko, taille n x n
    neko_nums = [list(map(int, input().split())) for _ in range(n)]

    # Lecture des m cartes tirées
    cards = [int(input()) for _ in range(m)]

    # Pré-traitement : pour chaque joueur, créer une table pour retrouver la position dans la matrice
    # des nombres donnés.
    # Clé = nombre, valeur = (ligne, colonne)
    pos_usagi = {}
    pos_neko = {}

    for i in range(n):
        for j in range(n):
            pos_usagi[usagi_nums[i][j]] = (i, j)
            pos_neko[neko_nums[i][j]] = (i, j)

    # On va conserver 2 matrices booléennes indiquant si le nombre correspondant est "marqué"
    marked_usagi = [[False]*n for _ in range(n)]
    marked_neko = [[False]*n for _ in range(n)]

    # Fonction pour calculer combien de lignes droites d'au moins n éléments sont marquées.
    # Ici, on veut compter combien de lignes contenant exactement n "marqués" sont alignées en ligne,
    # colonne ou diago.
    # Mais en fait, on cherche le nombre de ligne droite avec longueur n seulement.
    # Ici, la victoire est définie par le nombre de lines (chaque ligne est une ligne = n éléments)
    #  - Remarque : dans ce problème la ligne droite d'une n-uplet sur la même ligne/colonne/diagonale, 
    #    si le joueur a marqué T nombres alignés, ça vaut 1 si T==n, sinon 0.

    # Donc en réalité, forcer la forme du problème: on compte combien de lignes, colonnes, ou diagonales
    # entières sont marquées (composées de n éléments) = cela donne un entier count.
    # On compte combien de lignes de cette sorte sont présentes pour chaque joueur.

    # Pour un joueur, retourner le nombre de lignes droites de longueur n entièrement marquées.

    def count_lines(marked):
        count = 0
        # Lignes
        for i in range(n):
            if all(marked[i][j] for j in range(n)):
                count += 1
        # Colonnes
        for j in range(n):
            if all(marked[i][j] for i in range(n)):
                count += 1
        # Diagonale principale
        if all(marked[i][i] for i in range(n)):
            count += 1
        # Diagonale secondaire
        if all(marked[i][n - 1 - i] for i in range(n)):
            count += 1
        return count

    # Suivi de l'état de la partie
    # À chaque tirage de carte, on marque pour Usagi et Neko si le nombre est présent
    # On teste si l'un d'eux remplit la condition de victoire (>= u ou >= v)
    # On rend le verdict dès que possible (seulement si un joueur gagne seul à ce moment)

    winner = None

    for c in cards:
        # Marquer pour Usagi
        if c in pos_usagi:
            x, y = pos_usagi[c]
            marked_usagi[x][y] = True
        # Marquer pour Neko
        if c in pos_neko:
            x, y = pos_neko[c]
            marked_neko[x][y] = True

        # Vérifier victoires seulement si pas de victoire déjà déclarée
        if winner is None:
            usagi_count = count_lines(marked_usagi)
            neko_count = count_lines(marked_neko)

            # Vérifier conditions de victoire
            usagi_win = (usagi_count >= u)
            neko_win = (neko_count >= v)

            # Cas où l'un seul a gagné => décidez le gagnant
            if usagi_win and not neko_win:
                winner = "USAGI"
            elif neko_win and not usagi_win:
                winner = "NEKO"
            # Si les deux ont gagné simultanément ou aucun alors on continue

    # Si aucun vainqueur unique apparu durant les tirages => DRAW
    if winner is None:
        winner = "DRAW"

    print(winner)


if __name__ == "__main__":
    main()