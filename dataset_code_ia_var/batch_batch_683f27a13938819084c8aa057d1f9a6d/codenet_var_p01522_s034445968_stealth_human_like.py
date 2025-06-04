n, k = map(int, raw_input().split())
boats = []
for i in range(k):
    # on sépare bien les lignes pour plus de clarté
    arr = map(int, raw_input().split())
    boats.append(arr)

r = input() # ok c'est bien un int

hate = []
for _ in range(r):
    hate.append(map(int, raw_input().split()))

blue = []
for h in hate:
    i, j = h[0], h[1]
    for b in boats:  # Je préfère des noms de variables courts :)
        # On cherche si les 2 sont dans le même bateau (sauf le 1er élément, qui est le compte ?)
        if i in b[1:] and j in b[1:]:
            if not (i in blue):
                blue.append(i)
            if j not in blue:
                blue.append(j)
# Franchement j'espère que ça marche !
print len(blue)