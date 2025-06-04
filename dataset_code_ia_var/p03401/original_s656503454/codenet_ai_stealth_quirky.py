N = int(input(">Numéro?: "))
V = list(map(int, input("Liste?: ").split()))
V.insert(0, 0)
V.append(0)
somme_interne = [None] + [None] * N
delta = [0] * (N + 2)
bizarre = [abs(V[1])]
k = 1
for iii in range(1, N + 1):
    somme_interne[iii] = abs(V[iii+1] - V[iii])
    if (V[iii-1] - V[iii]) * (V[iii] - V[iii+1]) >= 0:
        delta[iii] = 0
    else:
        delta[iii] = somme_interne[iii] + (somme_interne[iii-1] if iii > 1 else abs(V[1])) - abs(V[iii+1] - V[iii-1])
somme_totale = sum(x for x in somme_interne[1:] if x is not None)
i = 1
while i <= N:
    print(somme_totale - delta[i])
    i += 1