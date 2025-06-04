n, m = map(int, raw_input().split())
resultat = 0
for i in range(n):
    ligne = map(int, raw_input().split())
    if i != 0:
        nouvelle_ligne = []
        for e in ligne:
            nouvelle_ligne.append(e ^ 1)
        ligne = nouvelle_ligne

    max_val = 0
    if m > 2:
        for j in range(1, m-1):
            s = ligne[0] + ligne[-1]
            for k in range(1, m-1):
                if k == j:
                    s += (ligne[k] ^ 1 ^ 1)
                else:
                    s += (ligne[k] ^ 1)
            if s > max_val:
                max_val = s
    else:
        max_val = 0

    temp1 = ligne[0]
    for e in ligne[1:]:
        temp1 += e ^ 1

    temp2 = ligne[-1]
    for e in ligne[:-1]:
        temp2 += e ^ 1

    if temp1 > max_val:
        max_val = temp1
    if temp2 > max_val:
        max_val = temp2

    resultat += max_val

print resultat