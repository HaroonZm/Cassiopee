n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

m = 0
for i in range(n):
    a_i = a[i] - 1
    m += b[a_i]
    if i > 0:
        if a[i] == a[i-1]+1:
            m += c[a[i-1] - 1]

print(m)