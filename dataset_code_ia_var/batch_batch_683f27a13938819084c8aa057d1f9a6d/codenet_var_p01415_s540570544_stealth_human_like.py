# Bon, on commence par lire nos paramètres
N, K, T, U, V, L = [int(val) for val in input().split()]
# s pour somme, c et h pour compte et ??? (je ne sais plus)
s = 0
c = 0
h = 0  # pour les piles en cours ?
# On pré-calcule parce qu’on va en avoir besoin tout le temps
TV = T * V

# Allez, on lit les distances (je ne sais plus pourquoi tout de suite)
D = []
for i in range(N):
    D.append(int(input()))
# dernier bout pour finir la route
D.append(L)

r = D[0]  # Je suppose que c’est la distance initiale (ou pas)
for i in range(N):  # Bon, on va étape par étape
    h += 1
    if h > K:
        h -= 1  # On ne peut pas dépasser K... normal non ?
        c = TV
    Ds = D[i+1] - D[i]  # Distance entre deux trucs
    # Gestion du carburant (ou des ressources ?)
    if c > 0:
        if Ds > c:
            Ds -= c
            s += c
            c = 0
        else:
            c -= Ds
            s += Ds
            Ds = 0
    # Si il reste encore de la distance à couvrir
    while Ds > 0 and h > 0:
        h -= 1
        if Ds > TV:
            Ds -= TV
            s += TV
        else:
            c = TV - Ds
            s += Ds
            Ds = 0
    if Ds > 0:
        r += Ds  # On accumule ce qui reste ? À revoir...

# Ah zut, il faut transformer r et s : les divisions sont pas très explicites
r = r / U
s = s / V

# Bon, print final, croisons les doigts
print(r + s)