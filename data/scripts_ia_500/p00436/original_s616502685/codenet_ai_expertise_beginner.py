n = int(input())
s = []
for i in range(1, 2 * n + 1):
    s.append(i)

m = int(input())
for _ in range(m):
    a = int(input())
    if a != 0:
        s = s[a:] + s[:a]
    else:
        new_s = []
        for i in range(n):
            new_s.append(s[i])
            new_s.append(s[i + n])
        s = new_s

for num in s:
    print(num)