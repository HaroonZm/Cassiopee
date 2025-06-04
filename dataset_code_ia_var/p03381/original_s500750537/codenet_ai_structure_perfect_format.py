def main():
    n = int(input())
    x = list(map(int, input().rstrip().split()))
    l, h = sorted(x)[n // 2 - 1 : n // 2 + 1]
    for i in x:
        if i <= l:
            print(h)
        else:
            print(l)

if __name__ == "__main__":
    main()