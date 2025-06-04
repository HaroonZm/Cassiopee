n = int(input())
a = []
for _ in range(n):
    a.append(input().strip())
perms = []
for i in range(n):
    for j in range(n):
        if i != j:
            perms.append(a[i] + a[j])
perms.sort()
print(perms[2])