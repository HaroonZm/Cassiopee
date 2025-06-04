N = int(input())
koma = list(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))

# Ajouter un zéro à la fin de la liste koma
koma.append(0)

for i in range(M):
    idx = order[i] - 1
    koma[idx] = koma[idx] + 1
    if koma[idx] == koma[idx+1] or koma[idx] == 2020:
        koma[idx] = koma[idx] - 1

# Supprimer le dernier élément ajouté (le zéro)
koma.pop()

for num in koma:
    print(num)