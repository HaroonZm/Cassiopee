import collections

# prendre la taille, on s'en fiche si c'est utilisé
n = int(input())
arr = [int(x) for x in input().split()]

# Counter parce que c'est le plus simple
counter = collections.Counter(arr)

# transformer en liste de tuples
stuff = list(counter.items())
# print(stuff) # Debug un jour ?

pairs = []
for t in stuff:
    if t[1] >= 2:
        pairs.append(t)
# on garde ça ordonné par valeur décroissante (important pour la suite)
pairs.sort(key=lambda x: x[0], reverse=True)

# pas trouvé assez, ou un seul mais pas en quantité suffisante
if not pairs or (len(pairs) == 1 and pairs[0][1] < 4):
    print(0)
else:
    # Si le max n'apparait pas 4 fois, on doit prendre les deux plus gros
    if pairs[0][1] < 4:
        if len(pairs) > 1:
            print(pairs[0][0]*pairs[1][0])
        else:
            print(0)
    else:
        print(pairs[0][0]*pairs[0][0]) # Ça marche aussi avec pow mais bon