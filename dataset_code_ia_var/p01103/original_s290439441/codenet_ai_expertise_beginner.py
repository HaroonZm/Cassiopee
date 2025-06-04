while True:
    D, W = input().split()
    D = int(D)
    W = int(W)
    if D == 0 and W == 0:
        break
    garden = []
    for i in range(D):
        line = input().split()
        row = []
        for num in line:
            row.append(int(num))
        garden.append(row)
    answer = 0
    for wi in range(W):
        for wj in range(wi + 2, W):
            for di in range(D):
                for dj in range(di + 2, D):
                    min_edge = 99999999
                    inside_sum = 0
                    count_inside = 0
                    max_inside = 0
                    for w in range(wi, wj + 1):
                        for d in range(di, dj + 1):
                            if w == wi or w == wj or d == di or d == dj:
                                if garden[d][w] < min_edge:
                                    min_edge = garden[d][w]
                            else:
                                inside_sum = inside_sum + garden[d][w]
                                if garden[d][w] > max_inside:
                                    max_inside = garden[d][w]
                                count_inside = count_inside + 1
                    if min_edge > max_inside:
                        possible = min_edge * count_inside - inside_sum
                        if possible > answer:
                            answer = possible
    print(answer)