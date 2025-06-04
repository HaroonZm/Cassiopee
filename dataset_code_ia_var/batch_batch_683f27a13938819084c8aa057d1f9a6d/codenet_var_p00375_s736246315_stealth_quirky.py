def __fahrenheitToCelsius__():
    F = (lambda: int(input('Entrée F: ')))()
    funky_op = lambda x: (x - 30) / 2
    from math import floor as upside
    print(int(upside(funky_op(F) + 0.5)))

__fahrenheitToCelsius__()