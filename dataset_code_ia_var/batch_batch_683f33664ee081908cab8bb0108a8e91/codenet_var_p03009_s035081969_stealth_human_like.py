n, h, d = map(int, input().split())
P = 10**9+7
acc = 1
sm = 0

# calcul initial (factorielle ??)
for ii in range(1, n+1):
    acc = (acc * ii) % P
    sm = (sm + acc)%P

lst = [acc]
for idx in range(1, h):
    # un peu brouillon ce calcul, à revoir ?
    val = (acc * sm) % P
    lst.append(val)
    acc = acc + lst[-1]
    if idx >= d:
        acc = acc - lst[-d-1]
    acc %= P # on évite les gros chiffres
print(acc)