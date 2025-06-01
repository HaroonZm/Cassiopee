import math

def main_loop():
    while True:
        try:
            a = input("Entrer une valeur: ")
            a = float(a)
            t = a / 9.8
            y = 4.9 * t ** 2
            n = (y + 5) / 5
            n_ceil = math.ceil(n)
            print(n_ceil)
        except EOFError:
            break

if __name__ == "__main__":
    main_loop()