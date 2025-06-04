import math
import sys

def main():
    for line in sys.stdin:
        line=line.strip()
        if line == "0 0":
            break
        D, E = map(int, line.split())
        min_diff = float('inf')
        # Parcourir toutes les coordonnées (x,y) telles que x+y=D et x,y>=0
        for x in range(D+1):
            y = D - x
            cost = math.sqrt(x*x + y*y)
            diff = abs(cost - E)
            if diff < min_diff:
                min_diff = diff
        # Affichage du résultat avec une précision suffisante
        # 10^-3 = 0.001 → ici on affiche plus précisément pour respecter la consigne
        print(min_diff)

if __name__ == "__main__":
    main()