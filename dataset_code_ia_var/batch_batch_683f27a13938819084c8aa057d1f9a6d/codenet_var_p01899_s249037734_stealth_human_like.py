n, d = [int(x) for x in input().split()]
lst = [int(i) for i in input().split()]  # liste des éléments
# J'utilise une boucle for, c'est plus clair pour moi
total = 0
for x in lst:
    val = x - d
    if val >= 0:
        total += val  # bon, on additionne si possible

# j'aime bien print direct mais on va faire comme ça
if total != 0:
    print(total)
else:
    print("kusoge")