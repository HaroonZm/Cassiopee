N = int(input())
X = list(map(int, input().rstrip().split()))
av = (2 * sum(X) + N) // N // 2
ans = 0
for x in X:
    ans += (x - av) ** 2
print(ans)