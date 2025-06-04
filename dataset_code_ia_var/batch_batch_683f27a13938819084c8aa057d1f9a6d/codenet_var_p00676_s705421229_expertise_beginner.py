import math

while True:
    try:
        valeurs = raw_input().split()
        a = int(valeurs[0])
        l = int(valeurs[1])
        x = int(valeurs[2])
    except EOFError:
        break
    # Calcul de ADC
    milieu = (l + x) / 2.0
    ADC = math.sqrt(milieu * milieu - (l / 2.0) * (l / 2.0)) * l / 2
    # Calcul de ABC
    ABC = math.sqrt(l * l - (a / 2.0) * (a / 2.0)) * a / 2
    # Affichage du résultat
    print ABC + 2 * ADC