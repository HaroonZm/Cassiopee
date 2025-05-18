N = 1407; K = 38
ans = []
for i in range(K):
    tmp = [1] + list(range((K-1)*i+2, (K-1)*(i+1)+2))
    ans.append(tmp)
for i in range(1, K):
    for j in range(K-1):
        tmp = [i+1]
        for k in range(K-1):
            tmp.append(K+((j + (i-1)*k) % (K-1))+k*(K-1) + 1)
        ans.append(tmp)
print(N, K)
for l in ans:
    print(*l)