while True:
    n,m = map(int,input().split(" "))
    if n == 0:
        break

    items = []
    for i in input().split(" "):
        items.append(int(i))

    #全探索
    items2 = items
    sums = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i == j:
                continue
            sums.append(items[i] + items2[j])

    sums.sort(reverse=True)
    for i in range(len(sums)):
        if sums[i] <= m:
            print(sums[i])
            break
        if i == len(sums) - 1:
            print("NONE")