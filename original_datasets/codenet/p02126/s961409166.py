n, m, c = map(int, input().split())
l = [0] + list(map(int, input().split()))
w = [tuple(map(int, input().split())) for _ in range(n)]
w.sort(key = lambda x:x[1], reverse = True)
v = 0
p = 0
for i in range(n):
    if l[w[i][0]]:
        l[w[i][0]] -= 1
        v += w[i][1]
        p += 1
        if p == m:
            break
print(v)