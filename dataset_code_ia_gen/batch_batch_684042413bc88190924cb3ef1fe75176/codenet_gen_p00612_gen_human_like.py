def main():
    while True:
        N = int(input())
        if N == 0:
            break
        # Le nombre total de carreaux (tiles) dans la paroi interne est :
        # Les six faces du pavé droit :
        # - Haut et bas : 2 faces de N x N chacune
        # - Quatre faces latérales : 4 faces de N x 2 chacune
        # Donc total tiles = 2 * N * N + 4 * N * 2 = 2*N^2 + 8*N

        # Après rotation, seules les tuiles où la casserole touche le liquide doivent être comptées.
        # Cependant, selon l'énoncé, une fois la rotation effectuée jusqu'à uniformisation,
        # la zone touchée correspond aux tuiles sur la surface du solide dilué.
        # Il s'avère que la solution correspond à la somme des surfaces latérales + superficie haut + bas,
        # multiplié par certains facteurs.

        # En analysant les résultats fournis (exemples)
        # N=2 -> output=24
        # N=4 -> output=64
        # On remarque que:
        # Pour N=2 : 2*N*N + 8*N = 2*4 + 16 = 8 +16 = 24
        # Pour N=4 : 2*16 + 32 = 32 + 32 = 64

        # Ainsi la réponse correspond au nombre total de tuiles couvrant toutes les faces.

        result = 2 * N * N + 8 * N
        print(result)

if __name__ == '__main__':
    main()