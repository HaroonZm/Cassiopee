import sys
input=sys.stdin.readline

N,R=map(int,input().split())
P=list(map(int,input().split()))

sorted_P=sorted(P)

red_positions=set()
blue_positions=set()

# On veut pouvoir, par échange entre même couleur, obtenir la séquence triée.
# Cela signifie que pour chaque position i,
# la couleur de P[i] doit être la même que celle de sorted_P[i]

# On cherche une coloration binaire (R rouges, N-R bleus)
# telle que pour tout i on ait couleur(P[i])=couleur(sorted_P[i])

# On associe les couleurs à P[i] en fonction de la couleur de sorted_P[i]

# Puis on compte combien de nombres sont rouges/bleus en fonction de sorted_P
# si ça correspond au R, c'est possible.

color = [0]* (N+1) # couleur de chaque nombre: 1 pour rouge, 0 pour bleu

# Les R premiers de sorted_P seront rouges, le reste bleus
for i in range(R):
    color[sorted_P[i]] = 1

for i in range(R,N):
    color[sorted_P[i]] = 0

# Vérifier si pour tout i, color[P[i]] == color[sorted_P[i]]
for i in range(N):
    if color[P[i]] != color[sorted_P[i]]:
        print("No")
        break
else:
    print("Yes")