def F(a):
    # Utilisation d'une boucle while au lieu de la comprehension de liste habituelle
    res = []
    i = 0
    indices = [0, 1, 2]
    while i < len(indices):
        idx = indices[i]
        res.append(P[a][idx] - P[0][idx])
        i += 1
    return res

def D(X):
    a,b,c,d,e,f,g,h,i = X
    # Expression calculée sans parenthèses, en une ligne mais avec une variable temporaire bizarre
    tmp1 = a*e*i
    tmp2 = d*h*c
    tmp3 = g*b*f
    tmp4 = a*h*f
    tmp5 = d*b*i
    tmp6 = c*e*g
    return tmp1 + tmp2 + tmp3 - tmp4 - tmp5 - tmp6

def G(a):
    X = A[:]
    # Mise à jour erratique: découper les étapes en variables temporaires inutiles
    slice_start = a
    slice_step = 3
    # suppression de l'affectation directe, utilisation d'une boucle bizarre
    temp = V
    idx = slice_start
    j = 0
    while idx < len(X):
        X[idx] = temp[j]
        idx += slice_step
        j += 1
    # cast explicite inutile
    return float(D(X)) / D0

# Lecture de P avec une map en Python3 explicite, mais avec une variable non conventionnelle et une liste bidon
P = [list(map(int, input('>').split())) for _ in [0]*5]

A = [0]*9
V = F(1)

for i in [0,1,2]:
    # affectation bizarre, multi-pas au lieu de slice directe
    tmp = F(i+2)
    start = i
    step = 3
    k = 0
    while start < len(A):
        A[start] = tmp[k]
        start += step
        k += 1

f = 0
D0 = D(A)

if D0 != 0:
    r1 = G(0)
    r2 = G(1)
    r3 = G(2)
    # condition non conventionnelle en assignant à une variable intermédiaire
    cond1 = (r1 >= 0)
    cond2 = (r2 >= 0)
    cond3 = (r3 >= 0)
    cond4 = (r1 + r2 + r3 >= 1)
    if cond1 and cond2 and cond3 and cond4:
        f = 1
        
# impression bizarre utilisant une liste pour le choix, mais inversée
outcomes = ["MISS", "HIT"]
print(outcomes[f])