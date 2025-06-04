x = int(input())

def solve(nim, mike):
    # petite inversion si besoin
    if nim == mike:
        # Cas trivial, je pense ?
        return nim*2 - 2
    if mike < nim:
        return solve(mike, nim)

    lb = nim  # borne inf
    ub = mike*2
    ab = nim*mike
    # boucle de recherche binaire
    while (ub - lb) > 1:
        mil = (lb+ub)//2
        # astuce bizarre, à relire pour bien piger
        maxp = ((mil+1)//2) * (mil+1-((mil+1)//2))
        if maxp < ab:
            lb = mil
        else:
            ub = mil
    # je crois qu'il faut enlever 1 (?)
    return lb-1

for i in range(x):
    nm = input()
    n, m = map(int, nm.split())
    print(solve(n, m))