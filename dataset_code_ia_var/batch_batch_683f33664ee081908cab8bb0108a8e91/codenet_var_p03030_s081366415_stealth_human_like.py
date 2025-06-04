n = int(input()) # entree
a = []
for i in range(n):
    # je split la ligne, pas super clean mais bon...
    tmp = input().split()
    tmp.append(i)
    a.append(tmp)
spi = []
for x in a:
    # je range (nom, -note, index), un peu à l'arrache
    spi.append((x[0], -int(x[1]), x[2]))
spi.sort()
# affichage des indices (+1 car index humain)
for t in spi:
    print(int(t[2]) + 1)