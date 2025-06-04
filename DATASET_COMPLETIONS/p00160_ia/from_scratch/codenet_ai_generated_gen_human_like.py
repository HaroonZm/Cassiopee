def calc_fee(size, weight):
    sizes = [60, 80, 100, 120, 140, 160]
    weights = [2, 5, 10, 15, 20, 25]
    fees = [600, 800, 1000, 1200, 1400, 1600]

    for i in range(len(sizes)):
        if size <= sizes[i]:
            if weight <= weights[i]:
                return fees[i]
            else:
                # If weight exceeds current weight limit, check next size
                # Except for the last size
                if i == len(sizes) -1:
                    return 0
                # Continue to next iteration to check next size
                # But if weight still too big after last, excluded
    return 0

while True:
    n = input().strip()
    if n == '0':
        break
    n = int(n)
    total = 0
    for _ in range(n):
        x, y, h, w = map(int, input().split())
        size = x + y + h
        fee = 0
        # We try all sizes in order to find where it fits by size and weight
        sizes = [60, 80, 100, 120, 140, 160]
        weights = [2, 5, 10, 15, 20, 25]
        fees = [600, 800, 1000, 1200, 1400, 1600]
        for i in range(len(sizes)):
            if size <= sizes[i] and w <= weights[i]:
                fee = fees[i]
                break
            # if size <= sizes[i] but weight > weights[i], check next size
            # if size or weight don't match any category, fee remains 0
        total += fee
    print(total)