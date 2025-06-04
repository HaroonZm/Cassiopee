n = int(input())
a = [input().strip() for _ in range(n)]

perms = []
for i in range(n):
    for j in range(n):
        if i != j:
            perms.append(a[i] + a[j])

perms.sort()
print(perms[2])