n, m = [int(i) for i in input().split()]

b = [0 for i in range(n+1)]

for mi in range(m):
    b[int(input())] = 1
cnt = 0
s = [0 for i in range(n+1)]
s[0] = 1
if b[1] == 0:
    s[1] = 1
else:
    s[1] = 0
for ni in range(2,n+1):
    if b[ni] == 0:
        s[ni] = (s[ni-1] + s[ni-2]) % 1000000007
    else:
        s[ni] = 0
print(s[n])