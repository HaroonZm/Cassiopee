import sys
from bisect import bisect_right

# Bon, je vais garder input optimisé pour l'OJ sinon ça rame...
def input():
    return sys.stdin.readline()

def main(args):
    while True:
        d = int(input())
        if d == 0:
            break # on sort de la boucle, le cas 0 arrête le prog
        n = int(input())
        m = int(input())

        # Les positions des magasins sur le cercle (le 0 est omis au début, on l'ajoute après)
        lst = []
        for _ in range(n-1):
            lst.append(int(input()))
        # Ajout du magasin à la position 0 (point de départ/logique)
        lst.append(0); lst.append(d)
        lst.sort()  # Tri pour bisect

        # Les destinations des clients/du problème
        clients = []
        for _ in range(m):
            clients.append(int(input()))

        res = 0
        for dest in clients:
            # Si la destination est 0, pas la peine de faire quoi que ce soit (pourquoi ?)
            if dest == 0:
                continue

            idx = bisect_right(lst, dest)
            # un peu moche comme calcul mais bon...
            dist1 = dest - lst[idx-1]
            dist2 = lst[idx] - dest
            res += min(dist1, dist2)
            # fin de la boucle client

        print(res)
        # (j'oublie pas le print hein)

if __name__ == "__main__":
    main(sys.argv)  # pas sûr que args soit utile, mais bon