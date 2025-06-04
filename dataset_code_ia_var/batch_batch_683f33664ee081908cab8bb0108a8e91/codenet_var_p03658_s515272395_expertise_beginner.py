n_k = input().split()
N = int(n_k[0])
K = int(n_k[1])
l = input().split()
for i in range(N):
    l[i] = int(l[i])
l.sort()
l.reverse()
result = 0
for i in range(K):
    result = result + l[i]
print(result)