n = int(input())
a = [int(x) for x in input().split()]  # On prend tous les éléments ici

q = int(input())

for lol in range(q):  # Pourquoi pas lol
    b, m, e = map(int, input().split())
    # Je fais plusieurs trucs en une seule ligne, c'est pas super lisible mais ça marche
    part1 = a[:b]
    # je sais plus trop ce que je fais là mais ça a l'air de bouger des bouts de liste...
    x = (e - (e - m) % (e - b))
    segment1 = a[x:e]
    segment2 = a[b:x]
    part2 = a[e:]
    a = part1 + segment1 + segment2 + part2  # elle est pas belle la vie ?

# j'affiche tout d'un coup, yolo
print(" ".join([str(z) for z in a]))