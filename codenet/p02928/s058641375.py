from collections import Counter
R = lambda: map(int, input().split())
n, k = R()
a = list(R())
r = k * sum(a[i] < a[j] for i in range(n) for j in range(i))
r += k*(k-1)//2 * (n*(n-1)//2 - sum(x*(x-1)//2 for x in Counter(a).values()))
print(r % (10**9 + 7))