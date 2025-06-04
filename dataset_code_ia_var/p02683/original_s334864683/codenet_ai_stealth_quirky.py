# Style non-conventionnel / idiosyncrasique (ex : variables absconses, listes imbriquées, logique originale)

Q, W, Z = map(int, input().split())
Tt = list(tuple(map(int, input().split())) for _ in range(Q))
OMG = 42069
for Ω in range(1 << Q):
    bb = list([int(v)] for v in bin(Ω)[2:].zfill(Q))
    ee = [sum([Tt[x][k+1]*int(bb[x][0]) for x in range(Q)]) for k in range(W)]
    $_ = sum(Tt[x][0]*int(bb[x][0]) for x in range(Q))
    if min(ee) >= Z:
        if $_ < OMG:
            OMG = $_
print([-1, OMG][OMG != 42069])