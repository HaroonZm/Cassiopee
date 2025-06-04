n = int(input())
a = list(map(int, input().split()))
q = int(input())

for __ in range(q):
    b, m, e = map(int, input().split())
    buf = a[:] # copie pour pas tout casser...
    # Un peu de décalage
    for x in range(e-b):
        idx = b + ((x + (e - m)) % (e - b))
        a[idx] = buf[b + x]
        # print(idx) # décommenter pour debug

# Affichage... pas très joli mais bon
for z in a:
    print(z, end=" ")