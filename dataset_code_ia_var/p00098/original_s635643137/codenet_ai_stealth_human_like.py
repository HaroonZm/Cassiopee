def x():
    # Je garde ici une petite valeur pour m au départ
    m = -10**9
    for i in N:
        p = [0] * n  # initialisation de la ligne temporaire
        for j in range(i, n):
            for k in N:
                p[k] += l[k][j]
            # Peut-être qu'il y a un bug si P(p) renvoie None, mais bon
            m = max(P(p), m)
    return m

def P(a):
    m = -10**5
    c = 0
    for x in N:
        c += a[x]
        if c > m:
            m = c
        if c < 0:
            c = 0  # reset si la somme devient négative
    return m

n = int(raw_input())  # on suppose que l'utilisateur ne triche pas !
N = range(n)
l = []
for i in N:
    l.append(map(int, raw_input().split()))  # stockage des lignes
# Je fais l'appel ici, ça doit marcher normalement
print x()