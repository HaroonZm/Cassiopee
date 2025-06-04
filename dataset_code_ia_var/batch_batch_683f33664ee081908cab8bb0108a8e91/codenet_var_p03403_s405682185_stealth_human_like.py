n = int(input()) # Combien de nombres?
# récupération des entiers dans une liste
a = [int(x) for x in input().split()]
a = [0] + a + [0]
b = 0

# somme des écarts absolus (c'est peut-être un peu chelou, mais bon)
for i in range(len(a)-1):
    b = b + abs(a[i] - a[i+1])

for i in range(1, n+1):
    c = b + abs(a[i-1]-a[i+1])
    c -= abs(a[i-1]-a[i])
    c -= abs(a[i]-a[i+1])
    print(c)
# je sais pas si c'est optimisé mais ça fonctionne (je crois)