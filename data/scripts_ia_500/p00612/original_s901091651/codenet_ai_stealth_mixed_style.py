def f(n):
    res = 1 + 2 * n
    for i in range(1, int(n**0.5) + 1):
        res += 1 + ((n - i*i) // i) * 2
    return res

from sys import stdin

def main():
    lines = (line.strip() for line in stdin)
    while True:
        n = int(next(lines))
        if 0 == n:
            break
        print(8 * f(n // 2 - 1) + 8 * n)

if __name__ == "__main__":
    main()