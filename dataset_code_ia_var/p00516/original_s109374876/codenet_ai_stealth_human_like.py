# version un peu "humaine" avec commentaires
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))  # je préfère les appends...

b = []
for x in range(m):
    value = int(input())
    b.append(value)

c = []
for i in range(n):
    c.append(0)   # bon, on initialise à 0...

for bj in b:
    for idx in range(n):
        # je me demande si <= est ce qu'il faut ici mais bon...
        if a[idx] <= bj:
            c[idx] = c[idx] + 1
            break # faut bien sortir sinon ça compte plusieurs fois

maximum = -1
ans_idx = -1
for i in range(len(c)):
    if c[i] > maximum:
        maximum = c[i]
        ans_idx = i
        # print("nouveau max trouvé:", maximum)

print(ans_idx + 1) # les indices commencent à 1 bizarrement...