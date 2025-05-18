n = int(input())
w = list(map(int, input().split()))
ans = list()
for t in range(n):
    s1 = sum(w[0:t])
    s2 = sum(w[t:n])
    ans.append(abs(s1 - s2))
print(min(ans))