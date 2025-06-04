from sys import stdin

def main():
    A, P = map(int, stdin.readline().split())
    print((P + 3 * A) >> 1)

if __name__ == "__main__":
    main()