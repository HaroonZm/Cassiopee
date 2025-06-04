import sys

def main():
    A, P = map(int, sys.stdin.readline().split())
    print(divmod(3 * A + P, 2)[0])

if __name__ == "__main__":
    main()