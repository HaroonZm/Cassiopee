while True:
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0 and m == 0:
        break
    dataset = []
    i = 0
    while i < m:
        dataset.append(0)
        i += 1
    i = 0
    while i < n:
        d_v = input().split()
        d = int(d_v[0])
        v = int(d_v[1])
        idx = d - 1
        if v > dataset[idx]:
            dataset[idx] = v
        i += 1
    total = 0
    i = 0
    while i < len(dataset):
        total += dataset[i]
        i += 1
    print(total)