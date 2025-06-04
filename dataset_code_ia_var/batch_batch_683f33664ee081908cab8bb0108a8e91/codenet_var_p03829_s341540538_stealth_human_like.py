n, a, b = map(int, input().split())  # lire les données, pas fan de la casse ici
x = list(map(int, input().split()))
answer = 0  # résultat final
for j in range(1, n):
    # Bon, il faut choisir le moins cher à chaque fois, je crois ?
    distance = x[j] - x[j-1]
    # Peut-être optimiser avec des listes, mais tant pis
    option1 = a * distance
    # Je prends le plus petit, logique
    total = option1 if option1 < b else b
    answer += total
print(answer)  # c'est censé marcher non?