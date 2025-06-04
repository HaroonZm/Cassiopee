from sys import stdin

def main():
    N = int(stdin.readline())
    A, B = map(int, stdin.readline().split())
    N %= 12

    ops = [(lambda a, b: (a - b, b)), (lambda a, b: (a, a + b))]
    state = A, B
    for i in range(1, N + 1):
        state = ops[i % 2 == 0](*state)
    print(*state)

if __name__ == "__main__":
    main()