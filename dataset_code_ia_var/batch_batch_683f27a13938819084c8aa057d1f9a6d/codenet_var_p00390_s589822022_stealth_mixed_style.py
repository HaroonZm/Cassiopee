def get_vals():  # fonction utilitaire, style fonctionnel
    return list(map(int, input().split()))

N = input()
a = []
for i in get_vals():  # style impératif
    a.append(i)

w = get_vals()  # style compact

R = list(filter(lambda p: p[0] == 0, zip(a, w)))
L = []
for t in zip(a, w):  # boucle explicite
    if t[0] == 1:
        L.append(t)

minR = 0
if R:
    mR = 1e9
    for _, v in R:
        if v < mR:
            mR = v
    minR = mR

if len(L) > 0:
    minL = min([item[1] for item in L])
    print(int(minL + minR))
else:
    print(0)