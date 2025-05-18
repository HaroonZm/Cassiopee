while True:
    n, m = map(int, input().split())
    if not n and not m:
        break

    dataset = [0 for _ in range(m)]
    for i in range(n):
        d, v = map(int, input().split())
        dataset[d - 1] = max(v, dataset[d - 1])
    print(sum(dataset))