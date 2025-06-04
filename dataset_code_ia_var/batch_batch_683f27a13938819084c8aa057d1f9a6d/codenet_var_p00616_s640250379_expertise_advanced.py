from sys import stdin

def main():
    n_case = iter(stdin)
    for line in n_case:
        n, h = map(int, line.split())
        if n == 0:
            break
        occupied = set()
        for _ in range(h):
            c, a, b = next(n_case).split()
            a, b = int(a) - 1, int(b) - 1
            match c:
                case "xy":
                    occupied.update((a | (b << 9) | (z << 18)) for z in range(n))
                case "xz":
                    occupied.update((a | (y << 9) | (b << 18)) for y in range(n))
                case _:
                    occupied.update((x | (a << 9) | (b << 18)) for x in range(n))
        print(n ** 3 - len(occupied))

if __name__ == "__main__":
    main()