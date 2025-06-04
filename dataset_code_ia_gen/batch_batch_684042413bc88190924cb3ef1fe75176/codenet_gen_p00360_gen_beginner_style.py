s = input()
k = int(input())
s = list(s)
n = len(s)

for i in range(n):
    pos = i
    # Trouver le caractère le plus petit dans les k suivants
    for j in range(i + 1, min(n, i + k + 1)):
        if s[j] < s[pos]:
            pos = j
    # Déplacer le caractère à la position i en échangeant adjacent
    while pos > i and k > 0:
        s[pos], s[pos - 1] = s[pos - 1], s[pos]
        pos -= 1
        k -= 1
    if k == 0:
        break

print("".join(s))