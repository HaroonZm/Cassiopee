while True:
    N = int(input())
    if N == 0:
        break
    crops = []
    for _ in range(N):
        data = input().split()
        L = data[0]
        P = int(data[1])
        A = int(data[2])
        B = int(data[3])
        C = int(data[4])
        D = int(data[5])
        E = int(data[6])
        F = int(data[7])
        S = int(data[8])
        M = int(data[9])
        # total time: time to get all fruits for M times
        total_time = A + B + C + D + E
        total_time *= M
        # since it returns to leaf stage after producing fruit except last time
        if M > 1:
            total_time += (M - 1) * ( - E )
        # correction: explained - the cycle except fruiting (A+B+C+D+E), no doubling
        # actually total_time = A+B+C+D+E + (M-1)*(C+D+E) since after fruit, back to leaf (stage at C)
        # According to problem: after fruit, back to leaf stage (which is after C)
        # So each cycle except the first misses the seed to sprout and sprout to young leaf time
        # So total time:
        # first cycle: A+B+C+D+E
        # next cycles: (D+E+C)
        # (since from fruit it goes back to leaf, we add C+D+E for each next fruit)
        total_time = A + B + C + D + E + (M -1) * (C + D + E)
        income = F * S * M - P
        efficiency = income / total_time
        crops.append((L, efficiency))
    # sort by efficiency desc, then name asc
    crops.sort(key=lambda x: (-x[1], x[0]))
    for c in crops:
        print(c[0])
    print('#')