while True:
    try:
        w = float(input())
        if w <= 48.00:
            print("light fly")
        elif w <= 51.00:
            print("fly")
        elif w <= 54.00:
            print("bantam")
        elif w <= 57.00:
            print("feather")
        elif w <= 60.00:
            print("light")
        elif w <= 64.00:
            print("light welter")
        elif w <= 69.00:
            print("welter")
        elif w <= 75.00:
            print("light middle")
        elif w <= 81.00:
            print("middle")
        elif w <= 91.00:
            print("light heavy")
        else:
            print("heavy")
    except EOFError:
        break