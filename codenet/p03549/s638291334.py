def solve(string):
    n, m = map(int, string.split())
    return str(((n - m) * 100 + 1900 * m) * (2**m))

if __name__ == '__main__':
    print(solve(input()))