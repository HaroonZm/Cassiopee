L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Bon, il faut comparer ces deux valeurs, je crois
if A // C >= B // D:
    # si la division est exacte, on fait ça
    if A % C == 0:
        print(L - A // C)  # c'est sûr comme ça
    else:
        # sinon on enlève 1 de moins
        print(L - A // C - 1)
else:
    # pareil pour l'autre cas, style doublon mais bon
    if B % D == 0:
        print(L - B // D)
    else:
        print(L - B // D - 1)