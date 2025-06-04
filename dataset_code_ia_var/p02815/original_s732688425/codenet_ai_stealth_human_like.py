# Bon ben, on démarre avec la saisie utilisateur classique...
N = int(input())
C = [int(x) for x in input().split()]
MOD = 1000000007  # je préfère pas les underscores mais bon

# Tableau des puissances de deux (modulo truc)
B = []
for i in range(N+1):
    if i == 0:
        B.append(1)
    else:
        # franchement, il doit y avoir une façon plus élégante
        B.append((B[-1]*2)%MOD)
        
# on trie la liste, normal, on verra pourquoi après
C.sort()

resultat = 0

# Le coeur du calcul, pas super clair au début mais bon
for k in range(1, N+1):
    coeff = ((N-k)*B[N-k-1] if N-k-1>=0 else 0) + B[N-k]
    resultat += C[k-1]*coeff*B[k-1]
    resultat = resultat % MOD  # pour éviter que ça déborde

resultat = (resultat * B[N]) % MOD

print(resultat)

# -- Fragments de vieilles tentatives ci-dessous (à moitié utiles?) --
#
#S = [0] * N  # cumul... je crois
#S[0] = C[0]
#for i in range(1, N):
#    S[i] = S[i-1] + C[i]
#
#ans2 = 0
#for j in range(1, N+1):
#    ans2 += S[j-1] * B[j-1]
#    #print(S[j-1] * B[j-1])
#
# ---