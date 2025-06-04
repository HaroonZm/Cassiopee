import sys
sys.setrecursionlimit(10**7)

def main():
    # Lecture des données tant que H, W, N ne sont pas tous nuls
    while True:
        # Lire H, W, N
        H, W, N = map(int, sys.stdin.readline().split())
        if H == 0 and W == 0 and N == 0:
            break

        # Lire la grille initiale des directions
        # 0 -> Sud (down), 1 -> Est (right)
        grid = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

        # On va simuler la marche mais pas naïvement pour N fois (N peut être grand)
        # Solution efficace: utiliser la technique de "doublage" pour simuler plusieurs marches en O(logN)

        # Préparons une structure pour simuler une marche en partant de chaque case (i,j)
        # à travers les directions, on peut déterminer pour chaque position le point de sortie.

        # On veut calculer pour tout sommet (i,j) la position où on arrive après une seule promenade
        # Selon la règle:
        # On regarde la direction dans grid[i][j]
        # Si c'est 1 (Est), on remplace par 0 (Sud) et on va à (i, j+1)
        # Si c'est 0 (Sud), on remplace par 1 (Est) et on va à (i+1, j)

        # Comme on change la valeur à chaque passage, la position après k fois dépend de la modification des directions.

        # On remarque que l'évolution est déterministe et on peut modéliser chaque promenade comme une fonction f:
        # f: (i,j) -> (end_i, end_j)
        # et on veut f^N((1,1)) (N-ième promenade)

        # Implémentation de la technique de 'doublage' (binary lifting):
        # On calcule f^1, f^2, f^4, f^8,... jusqu'à la plus grande puissance de 2 <= N
        # Puis on compose ces fonctions pour obtenir f^N en O(log N)

        # Cependant, il faut aussi simuler la modification des directions:
        # On remarque que les directions à chaque intersection changent à chaque fois que l'on passe dessus.
        # La direction dépend donc de la parité du nombre de passages en cette case.

        # Un autre point important: Pour un même point (i,j),
        # la direction lors du k-ième promenade peut être déterminée par k mod 2

        # Par conséquent, on fait la modélisation suivante pour chaque intersection:
        # direction actuelle = initial_direction ^ (nombre_de_passages mod 2)

        # On peut donc représenter la position finale de la promenade en termes de N mod 2

        # La solution est donc:
        # - Tracer dans une première matrice la destination pour N=1 (puisque on fait une promenade)
        # - Construire des tables de transition pour les puissances de 2 jusqu'à la puissance maximale <= N
        # - Puis combiner en suivant l'exposant binaire de N pour trouver la position finale.

        # Pour cela, on va considérer un tableau "next_pos" de taille H x W qui contient la position
        # où on arrive après 1 promenade en partant depuis (i,j) en prenant en compte la direction initiale.

        # Nous allons gérer une matrice 0-based en Python mais correspondante à (1-based) du problème.

        # Construction du tableau next_pos:
        # next_pos[i][j] -> (i', j') où on arrive après avoir appliqué la règle du passage une fois.

        next_pos = [[(-1, -1) for _ in range(W)] for _ in range(H)]

        for i in range(H):
            for j in range(W):
                d = grid[i][j]  # initial direction: 0=S,1=E
                # Au passage, on inversera d pour la prochaine fois, mais là on simule un seul passage,
                # donc on part de d, et on va dans la direction correspondante.
                if d == 1:
                    # aller vers Est -> (i, j+1)
                    if j+1 <= W-1:
                        next_pos[i][j] = (i, j+1)
                    else:
                        # on est à la toute est donc arrêt, ici on notera position de sortie (i,j+1)
                        # La route la plus est est la colonne W, mais les croisements vont de 1 à W+1
                        # Le problème dit que les croisements vont jusqu'à W+1,
                        # donc on doit gérer la sortie en indiquant la coordonnée finale (i,j+2?).
                        # Mais on ne peut pas sortir du tableau, on se trouve sur la rue la plus à l'est.
                        # On devons arrêter, donc next_pos[i][j] = fin de promenade (i, j+1+1)
                        # On va gérer plus bas la fin de la promenade (quand on est sur limite).
                        # Pour la simulation, pos finale hors du tableau:
                        # On peut utiliser (i, W) si 0-based correspond à col W, qui est hors de la grille.
                        # En sortie on doit afficher en 1-based, la colonne j+2.
                        next_pos[i][j] = (i, W)
                else:
                    # aller vers Sud -> (i+1, j)
                    if i+1 <= H-1:
                        next_pos[i][j] = (i+1, j)
                    else:
                        # On est tout en bas -> même raisonnement que ci-dessus
                        next_pos[i][j] = (H, j)

        # Maintenant on construit la table de saut binaire (binary lifting).
        # max_power = max puissance de 2 <= N
        max_power = 1
        while max_power <= N:
            max_power <<=1
        max_power >>=1

        # On stockera les transitions pour 2^k promenades:
        # dp[k][i][j] = position finale après 2^k promenades en partant de (i,j)

        # Par souci de mémoire, on ne peut pas stocker dp pour tous k, i,j car H,W=1000 -> 1M elements, k peut être 24 ~ log2(10^7)

        # On va représenter dp par une liste de matrices. Stocker environ 25 matrices de 1000x1000 est possible en mémoire.

        dp = [next_pos]  # dp[0] correspond à 1 promenade

        # Construction dp pour les puissances supérieures
        # dp[k] = dp[k-1] o dp[k-1]
        # où o est la composition fonctionnelle

        # But: dp[k][i][j] = dp[k-1][dp[k-1][i][j]]

        k = 0
        while (1 << (k+1)) <= N:
            prev = dp[k]
            curr = [[(-1,-1) for _ in range(W)] for _ in range(H)]
            for i_ in range(H):
                for j_ in range(W):
                    pos1 = prev[i_][j_]
                    # pos1 peut être hors du tableau ==> on stocke position finale *comme cela*
                    # Si pos1 est hors de la grille (i>=H ou j>=W), dp[k][i][j] = pos1 (pas de changement)
                    i2, j2 = pos1
                    if i2 >= H or j2 >= W:
                        # terminaison, on reste sur cette position finale
                        curr[i_][j_] = pos1
                    else:
                        curr[i_][j_] = prev[i2][j2]
            dp.append(curr)
            k += 1

        # maintenant on applique la marche N fois en combinant les puissances de deux

        # position initiale = (0,0) en 0-based
        pos = (0,0)
        length = len(dp)
        current_power = 0
        # il faut décomposer N en binaire et appliquer la composition des dp correspondants

        exp = N
        for bit in range(length):
            if exp & (1 << bit):
                i_, j_ = pos
                if i_ >= H or j_ >= W:
                    # déjà en position finale
                    break
                pos = dp[bit][i_][j_]

        # pos peut être hors de la grille, on doit afficher 1-based.
        # La sortie indique la croisement finale (i,j) (1-based).
        # Dans le cas de sortie hors limite à droite ou en bas, on doit donner la position finale d'arrêt.

        # rappel: croisements sont de 1..H pour ligne, 1..W pour colonne
        # La position finale pos = (i,j) 0-based correspond à (i+1,j+1) 1-based
        # Si i == H (hors indice), cela correspond à la route la plus au sud, donc i+1 = H+1
        # Idem pour colonne j == W => j+1 = W+1

        i_final = pos[0] + 1
        j_final = pos[1] + 1

        print(i_final, j_final)

if __name__ == "__main__":
    main()