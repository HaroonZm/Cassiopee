from sys import stdin
from itertools import islice

def main():
    a, b = map(int, islice(stdin.readline().split(), 2))
    S = (a * b) / 3.305785
    print(f"{S:.6f}")

if __name__ == "__main__":
    main()