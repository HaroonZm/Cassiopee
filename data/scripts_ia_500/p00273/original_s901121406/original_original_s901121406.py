for i in range(input()):
    x, y, b, p = map(int, raw_input().split())
    cost1 = x * b + y * p
    cost2 = (x * max(b, 5) + y * max(p, 2)) * 0.8
    print "%d" % min(cost1, cost2)