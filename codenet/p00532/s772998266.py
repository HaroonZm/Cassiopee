n = int(input())
m = int(input())

a = list(map(int, input().split()))
p = [0]*n

for i in range(m):
    b = list(map(int, input().split()))
    for j in range(n):
        if a[i] == b[j]:
            p[j] += 1
        else:
            p[a[i]-1] += 1

for i in range(n):
    print(p[i])