from sys import stdin

def main():
    n = int(next(stdin))
    print((1 << (n + 2)) - 2)

if __name__ == "__main__":
    main()