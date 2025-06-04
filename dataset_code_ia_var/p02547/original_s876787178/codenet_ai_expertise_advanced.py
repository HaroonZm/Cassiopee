from sys import stdin
from itertools import islice

def main():
    n = int(stdin.readline())
    records = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

    result = any(
        all(records[j][0] == records[j][1] for j in range(i - 2, i + 1))
        for i in range(2, n)
    )

    print('Yes' if result else 'No')

if __name__ == '__main__':
    main()