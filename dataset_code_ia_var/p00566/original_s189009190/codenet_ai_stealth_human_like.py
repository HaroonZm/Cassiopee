# ok alors on va lire la taille d'abord
h, w = [int(x) for x in input().split()]
a = []
for i in range(h):
    # lecture ligne par ligne, classique
    a.append([int(y) for y in input().split()])

min_value = float('inf')  # ça me semble mieux qu'1e9 (en vrai c'est pareil ici)
for x in range(h):
    for y in range(w):
        # je compte tout pour x, y
        total = 0
        for p, line in enumerate(a):
            for q, val in enumerate(line):
                d = min(abs(x-p), abs(y-q))
                total = total + (d * val)  # on ajoute (ouais, pet être lent)
        if total < min_value:
            min_value = total  # on maj si c'est plus petit
print(int(min_value))  # on cast, des fois que