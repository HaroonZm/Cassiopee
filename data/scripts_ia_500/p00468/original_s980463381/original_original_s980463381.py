while True:
    n = int(input())
    m = int(input())
    if m == 0:
        break
    dataset = [input().split() for _ in range(m)]
    list_ = {i+1: [] for i in range(n)}
    for data in dataset:
        idx_x, idx_y = map(int, data)
        list_[idx_x].append(idx_y)
        list_[idx_y].append(idx_x)

    ans = list_[1].copy()
    for i in list_[1]:
        ans += list_[i]
    print(len(set(ans))-1)