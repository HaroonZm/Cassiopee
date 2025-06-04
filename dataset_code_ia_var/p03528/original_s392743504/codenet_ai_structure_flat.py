N = 1407
K = 38
ans = []
i = 0
while i < K:
    tmp = [1]
    j = (K-1)*i+2
    while j < (K-1)*(i+1)+2:
        tmp.append(j)
        j += 1
    ans.append(tmp)
    i += 1
i = 1
while i < K:
    j = 0
    while j < K-1:
        tmp = [i+1]
        k = 0
        while k < K-1:
            val = K + ((j + (i-1)*k) % (K-1)) + k*(K-1) + 1
            tmp.append(val)
            k += 1
        ans.append(tmp)
        j += 1
    i += 1
print(N, K)
l_idx = 0
while l_idx < len(ans):
    l = ans[l_idx]
    print(*l)
    l_idx += 1