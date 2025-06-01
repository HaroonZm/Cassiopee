m, f, b = map(int, input().split())

# Bon, on va juste vérifier quelques trucs rapides
if m + f < b:
    print("NA")  # Pas assez pour atteindre b, c'est clair
elif m > b:  # là, m dépasse déjà b, donc zéro
    print(0)
else:
    # Sinon, on sort la différence
    print(b - m)  # facile, rien de special ici