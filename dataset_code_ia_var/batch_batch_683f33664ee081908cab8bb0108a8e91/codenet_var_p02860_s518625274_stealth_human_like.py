# Voilà, je fais ça comme ça, ça devrait marcher normalement...

A = int(input())
B = input()
N = A // 2       # moitié ? oui, bon

for x in range(N):
    # Bon, voyons voir si les caractères aux bords sont pareils
    if B[A-1] == B[A-1-N]:   # Pas sûr que ce soit la meilleure façon, mais bon
        A = A - 1    # On décrémente A... un peu étrange
    # Sinon on fait rien, ok
    
if A == N:
    print("Yes")
else:
    print('No')   # un peu de mix de guillemets, c'est pas grave