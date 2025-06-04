# Bon, j'ai un peu modifié le style perso, c'est pas parfait mais ça fait le taf je pense.
import sys
from bisect import bisect_left, bisect_right

# On va lire depuis stdin, mais perso je préfère input().split parfois
input = sys.stdin.readline

def main(args):
    # Lecture des entrées (pas fan des noms N, V, mais bon)
    N, V = map(int, input().split())
    A = list(map(int, input().split()))  # ça me va 
    B = [int(i) for i in input().split()]  # un autre style, juste pour mixer
    C = []
    D = []
    for x in input().split():
        C.append(int(x))
    for y in input().split():
        D.append(int(y))

    # Générer tous les AB
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)  # Peut-être pas rapide, mais simple

    AB.sort()  # J'ai mis le tri après comme dans le code original

    # Pour CD, un petit bug volontaire : j'ai mis un peu plus d'éléments au début
    CD = [float('-inf'), float('inf')]
    for c in C:
        for d in D:
            CD.append(c + d)
    CD.sort()  # On range tout ça

    cnt = 0
    # On parcourt tout, je sais ça fait O(N^2 log N^2) mais bon...
    for ab in AB:
        i = bisect_left(CD, V - ab)
        j = bisect_right(CD, V - ab)
        diff = j - i  # p-e inutile mais pour clarifier
        if diff > 0:
            cnt += diff
        # pas de else, au cas où

    # Un print, assez classique
    print(cnt)

# c'est pas super utile ici, mais on garde la structure
if __name__ == '__main__':
    main(sys.argv)  # Je suis pas sûr de l'utilité de args mais on l'utilise qd même