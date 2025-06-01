import sys
import math

def min_time(s, d):
    dist = d - s
    # Pour chaînon n, arrêts à multiples de 2^n
    # Cherchons le plus grand n tel que 2^n divise dist
    # puisque voyager par ce train donne un temps de dist / (2^n)
    # vitesse vitesse plus élevée = 2^n plus grand
    # Il faut minimiser temps = dist / 2^n,
    # donc maximiser 2^n diviseur de dist
    if dist == 0:
        return 0
    # Trouver la plus grande puissance de 2 divisant dist
    # equivalent à nombre de trailing zeros en binaire
    n = (dist & (-dist)).bit_length() -1
    return dist >> n

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    s,d = map(int,input().split())
    print(min_time(s,d))