n = int(input())
a = list(map(int, input().split()))
a.sort()
N = a[-1]
half = N // 2

# Chercher l'indice de l'élément le plus proche de N//2 en restant strictement inférieur à N
indice = 0
for i in range(len(a)):
    if a[i] >= half:
        indice = i
        break
    indice = i

# Gérer les limites pour éviter les erreurs d'indice
chooser = []
if indice - 1 >= 0:
    chooser.append(a[indice - 1])
chooser.append(a[indice])
if indice + 1 < len(a):
    chooser.append(a[indice + 1])

plus_proche = None
plus_proche_diff = 10 ** 9
for val in chooser:
    if val < N:
        diff = abs(val - half)
        if diff < plus_proche_diff:
            plus_proche_diff = diff
            plus_proche = val

print(N, plus_proche)