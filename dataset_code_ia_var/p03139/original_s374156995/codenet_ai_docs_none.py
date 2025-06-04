def main():
    n, a, b = map(int, input().split())
    mx = min(a, b)
    if a + b > n:
        mn = a + b - n
    else:
        mn = 0
    print(mx, mn)

if __name__ == '__main__':
    main()