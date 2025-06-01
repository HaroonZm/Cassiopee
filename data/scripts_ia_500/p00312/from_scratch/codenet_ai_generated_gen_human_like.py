D, L = map(int, input().split())

# Nombre maximal de grands sauts possibles sans dépasser D
big_jumps = D // L
# Distance restante après les grands sauts
remainder = D % L

# Si la distance restante est zéro, alors le nombre total de sauts est juste les grands sauts
# Sinon, il faut ajouter des petits sauts (1 cm chacun)
if remainder == 0:
    print(big_jumps)
else:
    print(big_jumps + remainder)