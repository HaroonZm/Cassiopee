while True:

    try:
        boxer_weight_in_kilograms = float(input())

        if boxer_weight_in_kilograms <= 48:
            print('light fly')

        elif boxer_weight_in_kilograms <= 51:
            print('fly')

        elif boxer_weight_in_kilograms <= 54:
            print('bantam')

        elif boxer_weight_in_kilograms <= 57:
            print('feather')

        elif boxer_weight_in_kilograms <= 60:
            print('light')

        elif boxer_weight_in_kilograms <= 64:
            print('light welter')

        elif boxer_weight_in_kilograms <= 69:
            print('welter')

        elif boxer_weight_in_kilograms <= 75:
            print('light middle')

        elif boxer_weight_in_kilograms <= 81:
            print('middle')

        elif boxer_weight_in_kilograms <= 91:
            print('light heavy')

        else:
            print('heavy')

    except Exception:
        break