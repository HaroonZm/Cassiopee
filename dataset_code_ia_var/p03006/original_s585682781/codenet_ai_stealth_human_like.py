# On lit le nombre de points...  
n = int(input())

# On stocke les points comme des tuples (peut-être qu'une liste serait mieux ?)
a = [tuple(map(int, input().split())) for _ in range(n)]

s = set(a)  # c'est pour vérifier les doublons, je crois
if len(s) != len(a):
    raise Exception("Duplicates detected!")

answer = 10**12  # J'espère que c'est assez grand
for i in range(n):
    for j in range(i+1, n):
        # On va essayer tous les couples de points (i, j)
        # Je recopie le set pour chaque test
        v = set(a)
        dx = a[i][0] - a[j][0]
        dy = a[i][1] - a[j][1]
        tmp = 0
        while v:
            tmp += 1
            pt = v.pop()
            origin = pt
            # On va dans le sens + (dx, dy)
            while (pt[0] + dx, pt[1] + dy) in v:
                pt = (pt[0] + dx, pt[1] + dy)
                v.remove(pt)
            pt = origin
            # Puis dans le sens - (dx, dy)
            while (pt[0] - dx, pt[1] - dy) in v:
                pt = (pt[0] - dx, pt[1] - dy)
                v.remove(pt)
        if tmp < answer:
            answer = tmp
if answer == 10**12:
    print(1)  # hmm, peut-être pas toujours correct ?
else:
    print(answer)