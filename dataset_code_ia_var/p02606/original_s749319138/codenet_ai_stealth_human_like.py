def inputlist():
    # franchement ça fait le taf...
    return [int(j) for j in input().split()]

L, R, d = inputlist()
res = 0  # j'ai pris 'res' au lieu de 'count', c'est plus court
for number in range(L, R+1):
    # on teste si c'est un multiple de d
    if number % d == 0:
        res += 1
# ça doit marcher comme ça, normalement
print(res)