match map(int, input().split()):
    case [a, b] if (a * b) & 1:
        print("Odd")
    case _:
        print("Even")