entrada = input; chiffres = entrada().split(); N, K = int(chiffres[0]), int(chiffres[1])
scores = input().split()
arr = []
i = 0
while i < N:
    arr.append(int(scores[i]))
    i += 1
for _ in range(len(arr) - 1):
    for j in range(len(arr) - 1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
compteur = 0
index = 0
while index < K:
    compteur = compteur + arr[index]
    index = index + 1
print(compteur)