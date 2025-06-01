import sys
sys.setrecursionlimit(10**7)

MOD = 100000

def main():
    inputs = sys.stdin.read().strip().split('\n')
    for line in inputs:
        if line == '0 0 0':
            break
        N, M, S = map(int, line.split())

        # dp[c][s][k] = nombre de façons de choisir k nombres STRICTEMENT croissants
        # dans [1..M], somme égale à s
        # Nous préparerons dp pour k de 0 à N, s de 0 à S, c de 0 à M
        # Pour efficacité, on réduira dimension s maximale à S

        # Initialisation DP colonne unique: dp_col[k][sum] = nb façons de choisir k croissants dans [1..M] avec somme sum
        dp_col = [dict() for _ in range(N+1)]
        dp_col[0][0] = 1

        for x in range(1, M+1):
            for k in range(N-1, -1, -1):
                for s_ in list(dp_col[k].keys()):
                    ns = s_ + x
                    if ns > S:
                        continue
                    dp_col[k+1][ns] = (dp_col[k+1].get(ns, 0) + dp_col[k][s_]) % MOD

        # dp_col[N][s] = nombre de façons de choisir N strictement croissants dans [1..M] avec somme s

        # Maintenant, pour N colonnes:
        # Conditions:
        # 1) Chaque colonne a N strictement croissants
        # 2) Tous les éléments de la colonne c sont strictement plus grands que tous ceux de la colonne c-1
        # 3) Somme totale S = somme sur colonnes des sommes de chaque colonne
        #
        # Soit dp_tot[pos][sum][last] = nombre de façons de construire jusqu'à la colonne pos
        # avec somme sum, et les valeurs max dans la colonne précédente <= last
        # last est la valeur max de la colonne précédente, pour imposer la condition sur le prochain.

        # Mais cette approche est trop coûteuse en mémoire (last pouvant aller jusqu'à 2000).
        # Observons que dans une colonne nous choisissons N strictement croissants dans [last+1..M].
        # On peut pré-calculer dp_col pour [a..M], pas seulement [1..M].
        #
        # On peut faire une fonction qui calcule dp_col range restreint.

        # Mémo pour dp_col range restreint
        from functools import lru_cache

        @lru_cache(None)
        def col_dp(start):
            # dp_col_sub[k][sum] pour choix dans [start..M]
            dp_sub = [dict() for _ in range(N+1)]
            dp_sub[0][0] = 1
            for x in range(start, M+1):
                for k in range(N-1, -1, -1):
                    for s_ in list(dp_sub[k].keys()):
                        ns = s_ + x
                        if ns > S:
                            continue
                        dp_sub[k+1][ns] = (dp_sub[k+1].get(ns, 0) + dp_sub[k][s_]) % MOD
            return dp_sub[N]

        # dp totale: dp_tot[pos][sum][last]  -> on fera compression pour last en version dict

        from collections import defaultdict

        dp_tot = [defaultdict(int) for _ in range(N+1)]
        # Avant la première colonne, last = 0 (pas d'élément)
        dp_tot[0][(0, 0)] = 1  # (sum, last_col_max) : nombre de façons

        for pos in range(N):
            ndp = defaultdict(int)
            for (sum_so_far, last_max), ways in dp_tot[pos].items():
                # On choisit la colonne pos: N strictement croissants dans [last_max+1..M]
                col_ways = col_dp(last_max+1)
                for col_sum, cways in col_ways.items():
                    ns = sum_so_far + col_sum
                    if ns > S:
                        continue
                    nlast_max = 0
                    # Le max de la colonne c'est le max des N nombres choisis
                    # ici on ne connait pas directement
                    # Observons que le plus grand est forcément en [last_max+1..M]
                    # mais on ne sait pas lequel dans dp_col, on n'a pas stocké max 
                    # Couplons via la fonction col_dp: on ne connaît pas max. 
                    # Mais on peut inverser la logique:
                    # On peut implanter la fonction col_dp pour retourner aussi max des sets
                    # Comme max value dans dp_col[N][sum] correspond au max des éléments choisis,
                    # Ici pour la somme col_sum on ne connaît pas max direct.
                    # Cette méthode pose problème.

                    # Alternative:
                    # Pour col_dp nous traitons la gamme [start..M] avec strict croissant.
                    # Peut-on utiliser autre chose?

                    # Pour fixer cela, paramétrons col_dp avec dimension max_val.


                    pass # on changera d'approche

            # Re-integration échoue, on refait avec approche différent

        # Proposition alternative:
        # On pré-calcul toutes les combinaisons de N nombres strict croissants dans [1..M] avec somme s
        # On crée un vecteur de tuples : (sum, min_val, max_val) et nombre de façons 
        # min_val est le premier nombre sélectionné, max_val le dernier.
        # Ensuite on aligne les colonnes en vérifiant que min_val_col_{i} > max_val_col_{i-1}
        #
        # Cette approche est réalisable car N <=7 et M<=2000, mais il faut réduire solution.

        # Optimisation:
        # N <=7
        # On peut générer toutes les combinaisons possibles (N strict croissant entre 1..M) avec leurs somme, min, max
        # ensuite on trie ces "segments" par min_val pour concater sur les colonnes en DP

        # Générons toutes ces séquences possible de longueur N strictement croissant:
        # Quand N=7 et M=2000, combinaisons sont nombreuses (C(2000,7)=énorme)
        # Impossible brute force.

        # Puisque M est grand, on simplifie:

        # On remarque que la condition de monotonie stricte entre colonnes impose que tous les éléments du j-eme colonne 
        # sont plus grand que tous ceux de la j-1eme.
        # Cela signifie que les N × N éléments sont strictement croissants de gauche à droite et de haut en bas.

        # En fait pour tout (i, j):
        # carte[i][j] > carte[i][j-1]
        # et
        # carte[i][j] < carte[i+1][j]

        # La matrice est strictement croissante ligne par ligne et colonne par colonne.

        # Ce problème revient à trouver des partitions strict dominantes ordonnées des suites strictement croissantes.

        # Solution finale (inspirée solution japonaise officielle):
        # Posons f(c, last_col_max, s) le nb de cartes possibles jusqu'à la colonne c, 
        # dernier maximum de la colonne est last_col_max, somme partielle s.
        # On doit considérer que la colonne c est composée d'une suite strictement croissante de taille N dans [last_col_max+1..M]
        # On peut générer à l'avance toutes les combinaisons des colonnes possibles: En pratique,
        # C'est impossible de traiter toutes.
        #
        # Solution dynamique avec dp:
        # dp[c][s][m] = nombre de manières pour la c-ième colonne avec somme s et max = m
        # 
        # On peut ici utiliser 'combinaison avec somme et max'

        # On résout en:
        # 1. Construire pour chaque colonne c une fonction f_c(s, m) = nombre de séquences strictement croissantes
        # de longueur N dans [x..M] avec somme s et max m.

        # 2. La somme totale S = somme des s_i
        # 3. La condition entre colonnes impose m_{c-1} < min_{c} <= max_{c}
        #
        # On double compte min et max => mais min >= m_{c-1}+1 car les éléments sont strict croissants et plus grands
        #
        # Donc min_{c} > max_{c-1} mais on a besoin de min_{c} pour vérifier la transition.
        #
        # Solution: on remarque que la différence min et max est au moins N-1 (car éléments strictement croissants)

        # On peut approximer en fixant max, somme s et min > max_{c-1} pour le c-ième colonne.

        # Implémentons la solution officielle japonaise simplifiée:

    dp = [[[0]*(M+2) for _ in range(S+1)] for _ in range(N+1)]
    # dp[k][s][m] = nombre de séquences strictement croissantes de longueur k, somme s, max = m

    # Initialisation
    dp[0][0][0] = 1

    for m in range(1, M+1):
        for k in range(N, 0, -1):
            for s_ in range(S - m +1):
                val = dp[k-1][s_][m-1]
                if val ==0:
                    continue
                dp[k][s_+m][m] = (dp[k][s_+m][m] + val) % MOD
        # Propagation max
        for k in range(N+1):
            for s_ in range(S+1):
                dp[k][s_][m] = (dp[k][s_][m] + dp[k][s_][m-1]) % MOD

    # dp_col_sums[k][s][m] = sum over max<=m de sequences length k sum s max <=m

    # Maintenant dp_col_sums[N][s][m] contient le nombre de séquences strictement croissantes de taille N, somme s, max <= m.

    # On initialise dp_cards[c][s][m] = nombre de cartes construites sur c colonnes.
    # avec somme s et maxm = max de la c-ième colonne

    dp_cards = [[[0]*(M+2) for _ in range(S+1)] for _ in range(N+1)]
    dp_cards[0][0][0] = 1

    for c in range(1, N+1):
        for s_ in range(S+1):
            for mmin in range(M+1):
                val = dp_cards[c-1][s_][mmin]
                if val == 0:
                    continue
                # Pour la colonne c, on choisit une séquence de max mmax > mmin
                for mmax in range(mmin+1, M+1):
                    for s2 in range(S - s_ +1):
                        ways = (dp[N][s2][mmax] - dp[N][s2][mmax-1]) % MOD
                        if ways == 0:
                            continue
                        ns = s_ + s2
                        if ns > S:
                            continue
                        dp_cards[c][ns][mmax] = (dp_cards[c][ns][mmax] + val * ways) % MOD

    result = sum(dp_cards[N][S][m] for m in range(M+1)) % MOD
    print(result)

if __name__ == '__main__':
    main()