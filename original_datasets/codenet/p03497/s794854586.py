from collections import Counter
n, k = map(int, input().split())
*a, = map(int, input().split())

c = Counter(a)
kv = sorted(c.items(), key=lambda x: x[1], reverse=True)

if n <= k:
    print(0)
else:
    ans = n
    for i in range(k):
        try:
            ans -= kv[i][1]
        except:
            pass
    print(ans)