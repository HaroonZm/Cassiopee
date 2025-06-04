# On va déterminer si les droites AB et CD sont parallèles.
# Deux vecteurs sont parallèles si leur produit vectoriel vaut zéro.
# Le produit vectoriel en 2D de vecteurs u=(x1,y1) et v=(x2,y2) est x1*y2 - y1*x2.

def are_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calcul des vecteurs AB et CD
    ABx = x2 - x1
    ABy = y2 - y1
    CDx = x4 - x3
    CDy = y4 - y3
    # Calcul du produit vectoriel
    cross = ABx * CDy - ABy * CDx
    # Considérons une petite tolérance pour gérer les imprécisions flottantes
    epsilon = 1e-9
    return abs(cross) < epsilon

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        data = list(map(float, input().split()))
        x1, y1, x2, y2, x3, y3, x4, y4 = data
        if are_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()