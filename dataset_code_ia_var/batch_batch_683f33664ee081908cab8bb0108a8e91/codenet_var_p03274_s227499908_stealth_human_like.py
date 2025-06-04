# Bon, let's do it step by step... Variables pas top mais bon
n, k = map(int, input().split())
A = list(map(int, input().split())) # On met A en majuscules, pourquoi pas

minimum = 1e18 # Très grand nombre (presque l'infini lol)

for j in range(n - k + 1):
    first = A[j]
    last = A[j + k - 1] # espérons que l'indexation marche
    # Cas tout sur la gauche (derrière zéro)
    if last <= 0:
        temp = abs(first)
    # tout à droite ?
    elif first >= 0:
        temp = abs(last)
    else:
        # passage par zéro
        temp = abs(first)*2 + abs(last) # on va à gauche puis à droite
        temp2 = abs(last)*2 + abs(first) # inverse
        if temp2 < temp:
            temp = temp2
    # Peut-être minimum ici !
    if temp < minimum:
        minimum = temp

print(int(minimum))