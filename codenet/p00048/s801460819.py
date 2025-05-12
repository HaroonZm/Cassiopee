while True:
    try:
        w = float(input())
        if w <= 48:
            print('light fly')
        elif w <= 51:
            print('fly')
        elif w <= 54:
            print('bantam')
        elif w <= 57:
            print('feather')
        elif w <= 60:
            print('light')
        elif w <= 64:
            print('light welter')
        elif w <= 69:
            print('welter')
        elif w <= 75:
            print('light middle')
        elif w <= 81:
            print('middle')
        elif w <= 91:
            print('light heavy')
        else:
            print('heavy')
    except:
        break