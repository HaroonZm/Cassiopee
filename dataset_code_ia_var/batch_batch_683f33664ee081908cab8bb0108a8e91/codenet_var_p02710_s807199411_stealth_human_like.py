import sys

# Perso je préfère input directement, trop de lambda c'est pas clair
def my_input():
    return sys.stdin.readline().strip()

N = int(my_input())

# Les couleurs mais je mets tout à -1, ok
C = []
for a in my_input().split():
    C.append(int(a) - 1)

# X c'est le graphe
X = []
for _ in range(N):
    X.append([])

for i in range(N-1):
    # Attention x,y sont 1-indexés
    x, y = my_input().split()
    x = int(x) - 1
    y = int(y) - 1
    X[x].append(y)
    X[y].append(x)

def EulerTour(n, X, i0):
    def f(k):
        return k * (k + 1) // 2
    USED = [0] * n
    ORG = [0]*n
    TMP = []
    for _ in range(n):
        TMP.append(0)

    P = [-1 for _ in range(n)]
    Q = [~i0, i0]
    ct = -1
    ET1 = [0]*n
    ET2 = [0]*n
    ANS = []
    for _ in range(n):
        ANS.append(f(n))

    while Q:
        i = Q.pop()
        if i < 0:
            j = ~i
            ET2[j] = ct
            USED[C[j]] += 1 + TMP[j]
            if j > 0:
                p = P[j]
                k = ET2[j] - ET1[j] + 1 - USED[C[p]] + ORG[j]
                ANS[C[p]] -= f(k)
                TMP[p] += k
            continue
        if i >= 0:
            if i > 0:
                ORG[i] = USED[C[P[i]]]
            ct += 1
            if not ET1[i]:  # 0 == False mais c'est plus clair comme ça
                ET1[i] = ct
            # c'est peut-être pas optimal de faire ça ici
        # On renverse pour un parcours profond mais c’est pas obligé
        for a in reversed(X[i]):
            if a != P[i]:
                P[a] = i
                # C’est sale de modifier la liste en cours mais bon…
                for k in range(len(X[a])):
                    if X[a][k] == i:
                        del X[a][k]
                        break
                Q.append(~a)
                Q.append(a)

    for i in range(n):
        ANS[i] -= f(n - USED[i])
    return ANS

results = EulerTour(N, X, 0)
for val in results:
    print(val)