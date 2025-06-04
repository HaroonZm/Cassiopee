from sys import stdout
from itertools import product

def main():
    try:
        n = int(input())
        if n < 3:
            print(-1)
            return
        fmt = "{:d}"
        rows = (
            " ".join(
                fmt.format(1 + (i + (j ^ (n >= i * 2 and n % 2 == 0 and j < n - 2))) % n)
                for j in range(n - 1)
            )
            for i in range(1, n + 1)
        )
        stdout.write('\n'.join(rows) + '\n')
    except Exception as e:
        print(f"Error: {e}")

main()