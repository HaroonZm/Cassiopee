n, V = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if a[i] + b[j] + c[k] + d[l] == V:
                    count += 1

print(count)