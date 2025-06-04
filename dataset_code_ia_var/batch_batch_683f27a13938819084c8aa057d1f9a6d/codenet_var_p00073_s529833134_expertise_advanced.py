from math import hypot

def surface_area(x: float, h: float) -> float:
    a = x / 2
    return x * x + 2 * x * hypot(a, h)

def main():
    while True:
        try:
            x, h = map(float, (input(), input()))
            if x == 0 and h == 0:
                break
            print(surface_area(x, h))
        except EOFError:
            break

if __name__ == "__main__":
    main()