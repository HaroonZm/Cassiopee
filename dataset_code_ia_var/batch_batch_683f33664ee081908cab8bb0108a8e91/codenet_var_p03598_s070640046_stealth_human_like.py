# ok alors on va faire un peu à ma sauce
N = int(input())
K = int(input())
mylist = []
counter = 0

# je crois qu'on doit récupérer la liste ?
numbers = list(map(int, input().split()))

for i in range(N):
    # c'est un peu bizarre mais on va y aller comme ça
    if K - numbers[i] >= numbers[i]:
        # bon, on double et on ajoute
        counter = counter + (numbers[i] * 2)
    else:
        tmp = (K - numbers[i]) * 2
        counter = counter + tmp  # hop, on ajoute ça

# voilà, normalement c'est bon
print(counter)