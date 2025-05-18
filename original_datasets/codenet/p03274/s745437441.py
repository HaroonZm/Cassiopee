N, K = list(map(int, input().split()))
X = list(map(int, input().split()))

minus = []
plus = []

for x in X:
    if x < 0:
        minus.append(-x)
    else:
        plus.append(x)

minus.reverse()
ans = float('inf')

for i in range(min(K+1, len(minus)+1)):
    p = K - i
    if i == 0:
        if len(plus) >= p:
            ans = min(ans, plus[K-1])
    elif i == K:
        if len(minus) >= K:
            ans = min(ans, minus[K-1])
    else:
        if len(plus) >= p and len(minus) >= i:
            a = plus[p-1]
            b = minus[i-1]
            if a < b:
                ans = min(ans, 2 * a + b)
            else:
                ans = min(ans, b * 2 + a)

print(ans)