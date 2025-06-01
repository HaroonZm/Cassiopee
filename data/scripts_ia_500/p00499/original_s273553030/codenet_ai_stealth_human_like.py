import math

vals = []
for _ in range(5):
    # je prends les entrées une par une
    vals.append(int(input()))

# on fait un genre de calcul un peu bizarre avec math.ceil
part1 = math.ceil(vals[1] / vals[3])
part2 = math.ceil(vals[2] / vals[4])

results = [part1, part2]
results.sort()  # tri en place, plus rapide je crois

# soustraction finale, je prends le dernier élément (le plus grand)
print(vals[0] - results[-1])