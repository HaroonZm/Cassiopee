# ok alors je commence par lire les valeurs
N, K = map(int, input().split())
heights = list(map(int, input().split()))

# euh, je crois qu'il faut trier du plus grand au plus petit ici
heights.sort(reverse=True)

# je crois que je dois enlever les K premiers... ouais je pense
for i in range(K):
    if heights:
        heights.pop(0)

# on somme le reste des hauteurs...
result = 0
for h in heights:
    result += h
print(result)