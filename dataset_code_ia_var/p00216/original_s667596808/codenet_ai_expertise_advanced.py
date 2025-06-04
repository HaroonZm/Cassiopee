from functools import partial

def calc(a, b, n):
    match n:
        case n if n <= 10:
            return a - b
        case n if n <= 20:
            return a - (b + (n - 10) * 125)
        case n if n <= 30:
            return a - (b + 1250 + (n - 20) * 140)
        case _:
            return a - (b + 1250 + 1400 + (n - 30) * 160)

get_input = partial(int, input)
a, b = 4280, 1150

while (n := get_input()) != -1:
    print(calc(a, b, n))