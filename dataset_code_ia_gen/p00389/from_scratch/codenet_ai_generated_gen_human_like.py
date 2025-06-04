n, k = map(int, input().split())

blocks_used = 0
height = 0
blocks_in_stage = 1

while True:
    # le poids supporté par chaque bloc à cette étape
    # est égal au nombre total de blocs au-dessus divisé par le nombre de blocs dans l'étage actuel
    # la contrainte est que ce poids ne doit pas dépasser k
    # puisque le poids sur chaque bloc est égale à blocks_used / blocks_in_stage
    if blocks_used / blocks_in_stage <= k and blocks_used + blocks_in_stage <= n:
        blocks_used += blocks_in_stage
        height += 1
        blocks_in_stage += 1
    else:
        break

print(height)