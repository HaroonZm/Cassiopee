n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])

b = []
for i in range(n+1):
    b.append(0)

for i in range(m):
    x = int(input())
    b[x] = 1

s = []
for i in range(n+1):
    s.append(0)

s[0] = 1

if b[1] == 0:
    s[1] = 1
else:
    s[1] = 0

for i in range(2, n+1):
    if b[i] == 0:
        s[i] = (s[i-1] + s[i-2]) % 1000000007
    else:
        s[i] = 0

print(s[n])