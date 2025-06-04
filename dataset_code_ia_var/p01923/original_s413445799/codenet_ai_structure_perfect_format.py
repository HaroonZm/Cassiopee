while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    dataset = [0 for _ in range(m)]
    for i in range(n):
        d, v = map(int, input().split())
        dataset[d - 1] = max(dataset[d - 1], v)
    print(sum(dataset))