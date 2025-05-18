for _ in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    d = [0, 0]
    for i in range(1, n):d = [max(a[i] - a[i - 1], d[0]), max(a[i - 1] - a[i], d[1])]
    print(*d)