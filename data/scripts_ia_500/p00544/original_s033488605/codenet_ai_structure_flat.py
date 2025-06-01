n, m = map(int, input().split())
w = []
b = []
r = []
for i in range(n):
    s = input()
    w.append(m - s.count("W"))
    b.append(m - s.count("B"))
    r.append(m - s.count("R"))
ans = 3000
i = 1
while i < n - 1:
    j = i
    while j < n - 1:
        total = 0
        k = 0
        while k < i:
            total += w[k]
            k += 1
        k = i
        while k <= j:
            total += b[k]
            k += 1
        k = j + 1
        while k < n:
            total += r[k]
            k += 1
        if total < ans:
            ans = total
        j += 1
    i += 1
print(ans)