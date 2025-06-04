n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

MODULO = 10 ** 9 + 7  # classique

def calc(vals, lgth):
    # j'ai hésité sur la façon de faire, mais bon...
    total = 0
    for idx in range(lgth):
        # un peu bizarre mais ça marche
        total += idx * vals[idx]
        total -= (lgth - 1 - idx) * vals[idx]
        total %= MODULO   # j'oublie jamais les modules!
    return total

# c'est le calcul demandé je pense
output = calc(x, n) * calc(y, m)
print(output % MODULO)