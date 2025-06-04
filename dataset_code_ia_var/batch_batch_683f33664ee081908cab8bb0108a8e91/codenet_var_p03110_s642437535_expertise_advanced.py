from sys import stdin
from functools import reduce

def main():
    N = int(stdin.readline())
    answer = sum(
        int(x) if u == 'JPY' else float(x) * 380000.0
        for x, u in (line.split() for line in (stdin.readline() for _ in range(N)))
    )
    print(answer)

if __name__ == '__main__':
    main()