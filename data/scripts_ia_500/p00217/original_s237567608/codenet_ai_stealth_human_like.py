while True:
    n = int(input())
    if n == 0:
        break
    max_distance = 0
    identifier = None  # Just to keep track of the max p value
    for _ in range(n):
        p, d1, d2 = map(int, input().split())
        total_dist = d1 + d2
        if total_dist > max_distance:
            identifier, max_distance = p, total_dist
    print(identifier, max_distance)