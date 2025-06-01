def main():
    """
    Programme principal pour résoudre un problème de programmation dynamique.

    Le programme lit les entrées suivantes :
    - n : nombre d'éléments (boutiques).
    - t : temps total disponible.
    - s : temps interdit (intervalle interdit spécifique).

    Pour chaque élément, deux valeurs sont lues :
    - a : valeur associée à l'élément.
    - b : temps requis pour cet élément.

    Ensuite, il calcule la valeur maximale accumulée en respectant les contraintes
    temporelles et en évitant un intervalle interdit entre y - b et y.

    La solution est trouvée grâce à une table de programmation dynamique dp,
    où dp[x+1][y] représente la valeur maximale pouvant être obtenue en
    considérant les x premiers éléments et un temps maximum de y.

    La formule de récurrence :
    - dp[x+1][y] = max(
        dp[x][y],                    # ne pas prendre l'élément x
        dp[x+1][y-1],                # garder la meilleure valeur au temps y-1 (propagation)
        dp[x][y-B[x]] + A[x]         # prendre l'élément x si possible (pas dans l'intervalle interdit)
      )
    sauf si y-B[x] < s < y (cas interdit), alors on n'inclut pas l'élément x.
    """
    n, t, s = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # Initialisation de la table dp (dimensions : (n + 1) x (t + 1))
    # dp[x][y] : valeur maximale avec les x premiers éléments en temps y
    dp = [[0] * (t + 1) for _ in range(n + 1)]

    # Remplissage de la table dp
    for x in range(n):
        bx = B[x]  # temps requis pour l'élément x
        ax = A[x]  # valeur de l'élément x
        dpx = dp[x]
        dpx1 = dp[x + 1]
        for y in range(1, t + 1):
            # Vérification que l'on peut prendre l'élément x sans violer l'intervalle interdit
            if 0 <= y - bx and not (y - bx < s < y):
                # Cas où on peut prendre ou ne pas prendre l'élément x, ou propager la meilleure valeur
                dpx1[y] = max(dpx[y], dpx1[y - 1], dpx[y - bx] + ax)
            else:
                # On ne peut pas prendre l'élément x à ce temps y,
                # on propage donc la meilleure valeur sur y-1 ou non inclusion
                dpx1[y] = max(dpx[y], dpx1[y - 1])

    # Affichage de la valeur maximale atteignable avec tous les éléments et le temps t
    print(dp[n][t])

main()