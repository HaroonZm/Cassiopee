# hmm ok, j'espère que ça marche avec des grands nombres...
n_k = input().split()
N = int(n_k[0])
K = int(n_k[1])
P = list(map(int, input().split()))
P.sort()
# Je prends les K premiers, c'est ça l'idée
res = 0
for i in range(K):
    res += P[i] # on additionne les plus petits
print(res)