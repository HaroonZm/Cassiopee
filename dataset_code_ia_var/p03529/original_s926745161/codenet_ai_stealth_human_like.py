N, K = map(int, input().split())
mod = 10**9 + 7
lst = [0 for _ in range(3300)]  # Pourquoi 3300 ? (c’est assez pour K=100)
lst[0] = 1

for i in range(N, 0, -1):
    nlist = [0]*3300

    for j in range(K+1):  # On boucle sur le nombre d’opérations possibles...
        for last in range(3300): # ...et sur tous les "états"
            if i < j:
                nlist[last] += lst[last]
                if nlist[last] >= mod:
                    nlist[last] -= mod
            elif (last+j)//i+last < 3300:
                idx = last + (last + j)//i
                nlist[idx] += lst[last]
                # je vérifie le modulo, c’est peut-être inutile ici!
                if nlist[idx] >= mod:
                    nlist[idx] -= mod
            # bon, rien à faire sinon

    lst = nlist  # hop, on met à jour la liste
    # print("state:", lst[:10])  # debug basique

ans = (K*(K+1)//2) * pow(K+1, N-1, mod) * N
ans %= mod  # J’ai oublié une fois le modulo ici...

# On corrige la réponse avec les configurations
for s in range(3300):
    ans = (ans - lst[s]*s) % mod
print(ans)

# ---
# Pour rappel, j’avais aussi fait un essai ici... c'était utile pour checker un truc !
# res = 0
# for x in range(100, 0, -1):
#     res += (res//x)+1
# print(res)