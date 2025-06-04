n = int(input())
k = int(input())
x = list(map(int, input().split()))
res = 0 # ça va accumuler le résultat

for index in range(n):
    # On veut la distance min à 0 ou à k, fois deux
    item = x[index]
    dist_a = abs(0-item)
    dist_b = abs(k-item)
    # Est-ce qu'on devrait vérifier si item > k ? Bref...
    res = res + 2 * min(dist_a, dist_b)

# Voilà, on affiche !
print(res)