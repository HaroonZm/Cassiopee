nombre_maximum, limite_k = map(int, input().split())

nombre_sequence = 0
diviseur = 1
somme_sequence = 0

while True:

    # Vérification de la condition somme_sequence / diviseur <= limite_k
    # équivalent à somme_sequence <= diviseur * limite_k
    while diviseur * limite_k < somme_sequence:
        diviseur += 1

    if somme_sequence + diviseur > nombre_maximum:
        break

    somme_sequence += diviseur
    nombre_sequence += 1

print(nombre_sequence)