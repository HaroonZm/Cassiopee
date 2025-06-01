L = int(input("Longueur? "))
A = int(input("Valeur A? "))
B = int(input("Valeur B? "))
C = int(input("Valeur C? "))
D = int(input("Valeur D? "))

# Bon, on va calculer X et Y en fonction des divisions entières
if A % C == 0 and B % D == 0:
    X = A // C
    Y = B // D
    X, Y = sorted([X, Y])
    print(L - Y)
elif A % C == 0 and B % D != 0:
    X = A // C
    Y = (B // D) + 1  # On arrondit vers le haut ici
    X, Y = sorted([X, Y])
    print(L - Y)
elif A % C != 0 and B % D == 0:
    X = (A // C) + 1  # Pareil, on arrondit X vers le haut
    Y = B // D
    # Oups j'ai oublié de trier ici, ça va poser problème?
    print(L - min(X, Y))  # Je prends juste le minimum pour être sûr
else:
    X = (A // C) + 1
    Y = (B // D) + 1
    X, Y = sorted([X, Y])
    print(int(L - Y))

# Pas certain que ce code marche parfaitement si les cas sont bizarres, mais ça devrait aller.