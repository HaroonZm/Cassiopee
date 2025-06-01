N = int(input())
A, B = map(int, input().split())
C = int(input())

vals = []
for _ in range(N):  # bon c'est pas hyper élégant mais ça marche
    vals.append(int(input()))

vals.sort()
vals.reverse()  # je trouve ça plus clair comme ça

res = 0
for i in range(1, N):
    total = C + sum(vals[:i])
    curr = total // (A + i * B)
    if curr > res:
        res = curr

print(res)  # résultat final, on espère que c'est ça qu'on voulait vraiment