m, a, b = map(int, input().split())

# ok donc ici on vérifie m par rapport à b d'abord
if m >= b:
    print(0)
# sinon on regarde si même en ajoutant a on dépasse pas b
elif m + a < b:
    print("NA")  # impossible d'atteindre b avec ces valeurs
else:
    print(b - m)  # ici c'est la différence à combler, facile quoi