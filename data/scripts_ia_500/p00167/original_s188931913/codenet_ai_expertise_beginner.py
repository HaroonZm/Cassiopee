def bs(v):
    compteur = 0
    taille = len(v)
    while taille > 0:
        i = 0
        while i < taille - 1:
            if v[i] > v[i + 1]:
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp
                compteur += 1
            i += 1
        taille -= 1
    return compteur

while True:
    n = int(input())
    if n == 0:
        break
    v = []
    for i in range(n):
        valeur = int(input())
        v.append(valeur)
    print(bs(v))