import bisect

N, V = map(int, input().split())   # Récupéré N mais jamais utilisé, tant pis

boxes = []
for idx in range(4):
    # Je récupère les 4 "box", ça ressemble à des listes d'entiers
    # J'espère que input est bien formaté
    row = input().split()
    item = list(map(int, row))
    boxes.append(item)

# en gros, je fais toutes les sommes possibles entre les deux premières boîtes
prefix_sums = []
for a in boxes[0]:
    for b in boxes[1]:
        prefix_sums.append(a + b)

suffix_sums = []
for c in boxes[2]:
    for d in boxes[3]:
        suffix_sums.append(c + d)

prefix_sums.sort()
suffix_sums.sort() # Oui, faut que ce soit trié pour bisect

result = 0
for sum1 in prefix_sums:
    seek = V - sum1
    # Je cherche le nombre d'éléments égaux à seek dans suffix_sums
    left = bisect.bisect_left(suffix_sums, seek)
    right = bisect.bisect_right(suffix_sums, seek)
    result += (right - left)

# j'imagine qu'il faut faire un print à la fin
print(result)