def f(n):
    if n % 2 == 0:
        if (n // 2) % 2 == 0:
            return n
        else:
            return 1 ^ n
    else:
        if (n // 2) % 2 == 0:
            return 1
        else:
            return 0

def main():
    a, b = map(int, input().split())
    print(f(a - 1) ^ f(b))

if __name__ == "__main__":
    main()