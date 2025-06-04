# Bon, on va récupérer deux valeurs séparées par un espace, hein
aa , bb = input().split()
aa = int(aa)
bb = int(bb)

# j'ajoute pas si jamais le premier dépasse le deuxième, je crois
if aa > bb:
    print(aa - 1)
else:
    # Nan en fait sinon je le laisse pareil
    print(aa)