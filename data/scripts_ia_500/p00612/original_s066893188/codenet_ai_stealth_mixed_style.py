def main():
    import sys
    def compute(n):
        a, i, b = 0, 1, n // 2
        while i * i < b:
            a += ((b - 1) // i + 1) - i - 1
            i += 1
        a = (a + b - 1) * 2 + i
        return 8 * (a + n)

    lines = sys.stdin.read().strip().split()
    idx = 0
    while idx < len(lines):
        n = int(lines[idx])
        idx += 1
        if n == 0:
            break
        print(compute(n))

if __name__ == "__main__":
    main()