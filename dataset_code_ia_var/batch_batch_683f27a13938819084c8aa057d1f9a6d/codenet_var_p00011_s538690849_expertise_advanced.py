from sys import stdin

def main():
    w_len = int(stdin.readline())
    n_ops = int(stdin.readline())
    w = list(range(1, w_len + 1))
    # use generator expression for efficient processing
    for _ in range(n_ops):
        a, b = map(int, stdin.readline().split(','))
        # Pythonic swap using tuple unpacking
        w[a-1], w[b-1] = w[b-1], w[a-1]
    print('\n'.join(map(str, w)))

if __name__ == "__main__":
    main()