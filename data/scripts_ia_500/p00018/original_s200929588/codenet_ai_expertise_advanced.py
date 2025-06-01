n = list(map(int, input().split()))
while any(n[i] < n[i + 1] for i in range(len(n) - 1)):
    for i in range(len(n) - 1):
        if n[i] < n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
print(*n)