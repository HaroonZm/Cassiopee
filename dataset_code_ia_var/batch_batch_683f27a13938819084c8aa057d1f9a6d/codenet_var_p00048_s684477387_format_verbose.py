while True:

    try:

        boxer_weight_in_kilograms = float(input())

        if boxer_weight_in_kilograms <= 48.00:
            print("light fly")

        elif boxer_weight_in_kilograms <= 51.00:
            print("fly")

        elif boxer_weight_in_kilograms <= 54.00:
            print("bantam")

        elif boxer_weight_in_kilograms <= 57.00:
            print("feather")

        elif boxer_weight_in_kilograms <= 60.00:
            print("light")

        elif boxer_weight_in_kilograms <= 64.00:
            print("light welter")

        elif boxer_weight_in_kilograms <= 69.00:
            print("welter")

        elif boxer_weight_in_kilograms <= 75.00:
            print("light middle")

        elif boxer_weight_in_kilograms <= 81.00:
            print("middle")

        elif boxer_weight_in_kilograms <= 91.00:
            print("light heavy")

        else:
            print("heavy")

    except Exception:
        break