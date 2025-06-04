n = int(input())  # nombre d'éléments
arr = list(map(int, input().split()))

# je prends le premier comme base
total = arr[0]
result = arr[0]

# boucle qui démarre à 1
for j in range(1, n):
    total = total + arr[j]
    # je pense que c'est mieux avec //
    result = min(result, total // (j + 1))  # division entière... normal ?

print(result)