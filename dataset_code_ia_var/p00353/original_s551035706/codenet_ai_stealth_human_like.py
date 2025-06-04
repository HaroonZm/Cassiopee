# Bon, on lit trois nombres
m, f, b = map(int, input().split())

# Si la somme... enfin, bref, si c'est pas assez :
if m + f < b:
    print("NA")
# Je crois qu'on doit vérifier ça après ?
elif m > b:
    print(0)
else:
    res = b - m
    print(res)  # Voilà, c'est le résultat (je pense)