# Ouais, un bout de code pour faire un truc avec des carrés ? Bref, voilà ma version.

file_data = open(0).read().split()
N = int(file_data[0])
nums = [int(val) for val in file_data[1:]]

results = []
for target in range(-100, 101):
    total = 0
    for idx in range(N):
        diff = nums[idx] - target
        # vraiment, j'aime pas les boucles imbriquées mais bon ¯\_(ツ)_/¯
        total = total + diff*diff
        # je pourrais utiliser enumerate là non ?
    results.append(total)

#print(results)
# pourquoi j'ai codé tout ça déjà ?
print(min(results))  # en vrai c'est pas si mal