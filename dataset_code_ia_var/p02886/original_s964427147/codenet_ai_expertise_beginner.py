N = int(input())
d = input().split()
for i in range(len(d)):
    d[i] = int(d[i])
a = 0
for i in range(N):
    for j in range(i+1, N):
        a = a + d[i] * d[j]
print(a)