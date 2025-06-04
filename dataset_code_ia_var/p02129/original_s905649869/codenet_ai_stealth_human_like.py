# Hum, essayons de faire quelque chose de vaguement lisible... enfin, à ma façon

n = int(input())   # je suppose que c'est le nombre de lignes ? je garde le nom en minuscule
s = [0, 0, 0, 0, 0, 0]    # keep track, pas sûr du sens de chaque
ref = [[2,1,3], [1,3,2], [3,2,1], [2,3,1], [3,1,2], [1,2,3]]

for k in range(n):
    seq = list(map(int, input().split())) # récupère les valeurs genre 0 1 0 ...
    ids = [1,2,3] # toujours pareil, on commence de ça
    
    # bon ici je crois qu'on saute le premier? donc from 1 à machin
    for j in range(1, len(seq)):
        if seq[j] == 0: # swap les deux premiers
            tmp = ids[0]
            ids[0] = ids[1]
            ids[1] = tmp
            # print(ids) # debug inutile
        elif seq[j] == 1:
            ids[1], ids[2] = ids[2], ids[1]
        # sinon on touche à rien

    for z in range(len(ref)):
        if ids == ref[z]:
            s[z] = s[z] + 1

#print(s)   # on doit pas afficher ça mais bon c'est pratique pour debug

# la grosse condition chelou
if (s[5] > 0 or s[0] > 1 or s[1] > 1 or s[2] > 1 or
    (s[0] > 0 and s[1] > 0 and s[4] > 0) or
    (s[0] > 0 and s[2] > 0 and s[4] > 0) or
    (s[0] > 0 and s[2] > 0 and s[4] > 0) or   # répétition? je laisse
    (s[0] > 0 and s[1] > 0 and s[3] > 0) or
    (s[0] > 0 and s[2] > 0 and s[3] > 0) or
    (s[1] > 0 and s[2] > 0 and s[4] > 0) or
    (s[3] > 0 and s[4] > 0) or
    (s[3] > 2) or (s[4] > 2)):
    print("yes")
else:
    print("no")