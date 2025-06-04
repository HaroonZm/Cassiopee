import math

# Bon, on va commencer par lire ce qu'il faut...
N = int(input())
# On va convertir tout ça en tupl... pas sûr d'être obligé mais tant pis
P = tuple([int(x) for x in input().split()])
T = tuple([int(x) for x in input().split()])

result = 9999999999  # assez grand normalement

for i in range(0, math.ceil(N/T[0]) + 1):
    for j in range(0, math.ceil(N/T[1]) + 1):
        for k in range(0, math.ceil(N/T[2]) + 1):
            left = N - i*T[0] - j*T[1] - k*T[2]
            if left > 0:
                l = math.ceil(left / T[3])
            else:
                l = 0  # Bon, pas besoin d'en prendre plus
            cost = i*P[0] + j*P[1] + k*P[2] + l*P[3]
            if cost < result:
                result = cost
            # Peut-être faire un print pour debug mais flemme
print(result)  # et voilà, normalement ça roule