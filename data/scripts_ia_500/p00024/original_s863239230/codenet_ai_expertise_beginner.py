while True:
    try:
        vitesse_initiale = float(input())
    except EOFError:
        break
    temps = vitesse_initiale / 9.8
    hauteur = 4.9 * (temps ** 2)
    étage = (hauteur + 5) // 5 + 1
    print(int(étage))