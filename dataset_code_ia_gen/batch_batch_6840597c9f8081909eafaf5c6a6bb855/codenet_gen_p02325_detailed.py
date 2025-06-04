import math
import sys

def bitonic_tsp(points):
    """
    Calcule la distance du plus court parcours bitonique.
    
    points : liste de tuples (x, y) triés par x croissant.
    
    Retourne la distance minimale du tour respectant les contraintes:
    - Du point le plus à gauche au plus à droite en allant strictement vers la droite
    - Puis retour au point le plus à gauche en allant strictement vers la gauche
    - Tous les points sont visités au moins une fois
    """
    n = len(points)
    
    # Calcul de la distance euclidienne entre deux points
    def dist(i, j):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        return math.sqrt(dx*dx + dy*dy)
    
    # dp[i][j] : distance minimale d'un chemin bitonique visitant les points 0..max(i,j)
    # et terminant aux points i et j (i <= j), les chemins se croisent à droite
    dp = [[math.inf] * n for _ in range(n)]
    dp[0][1] = dist(0,1)
    
    # On remplit dp en utilisant la relation de récurrence:
    # si j > i+1, dp[i][j] = dp[i][j-1] + dist(j-1, j)
    # sinon (j == i+1), dp[i][j] = min_{k < i} dp[k][i] + dist(k, j)
    for j in range(2, n):
        for i in range(j-1):
            if i < j-1:
                # cas j > i+1, on allonge le chemin en partant de dp[i][j-1]
                dp[i][j] = dp[i][j-1] + dist(j-1, j)
            else:
                # cas j == i+1, on cherche le meilleur k < i pour fermer le chemin
                min_val = math.inf
                for k in range(i):
                    val = dp[k][i] + dist(k, j)
                    if val < min_val:
                        min_val = val
                dp[i][j] = min_val
    
    # On cherche la distance minimale du chemin bitonique qui visite tous les points,
    # la réponse est dp[i][n-1] + dist(i, n-1) où i < n-1
    res = math.inf
    for i in range(n-1):
        val = dp[i][n-1] + dist(i, n-1)
        if val < res:
            res = val
    
    return res


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    
    # Les points sont déjà triés par x par hypothèse
    result = bitonic_tsp(points)
    
    # Affichage avec une erreur inférieure à 0.0001
    print("{:.8f}".format(result))