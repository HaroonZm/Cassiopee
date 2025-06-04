import sys

def main():
    *_, (a, b) = iter(map(int, sys.stdin.read().split())), None
    print(f"{a * b / 3.305785:.6f}")

if __name__ == "__main__":
    main()