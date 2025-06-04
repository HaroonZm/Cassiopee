n = int(input())
A = [[int(i) for i in input().split()] for _ in range(n)]

total = 1 << n
gscore = [0] * total
dp = [0] * total

i = 0
while i < n:
    k = 0
    while k < (1 << i):
        k_xor = k ^ (1 << i)
        gscore[k_xor] += gscore[k]
        j = 0
        while j < len(A[i]):
            c = A[i][j]
            if (1 << j) & k:
                gscore[k_xor] += c
            j += 1

        # inline the subset iteration loop
        c = -(1 << 50)
        l = k
        first = True
        while True:
            l_xor = l ^ (1 << i)
            c = max(c, gscore[l_xor] + dp[k ^ l])
            if l == 0:
                break
            l = (l - 1) & k
        dp[k_xor] = c
        k += 1
    i += 1

print(dp[-1])