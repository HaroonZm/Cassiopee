def swapper(vals):
    # Valeurs par référence (puisque liste mutables)
    tmp = vals.pop()
    vals.insert(0, tmp)
    return vals

xyz = list(input().split())
swapped = swapper(xyz)
for i in range(len(swapped)):
    swapped[i] = str(swapped[i])
print(*swapped)