n = int(input())  # taille du tableau
row = []
for j in range(n):
    row.append(0)
row2 = list(map(int, input().split()))

for idx in range(n):
    # on remplit les valeurs en fonction de row2
    val = row2[idx] - 1
    row[val] = idx + 1

# affichage, un peu manuel...
for k in range(len(row)):
    print(row[k], end=" " if k != n - 1 else "\n")
# fin, ok