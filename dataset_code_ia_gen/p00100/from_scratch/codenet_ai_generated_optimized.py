while True:
    n = int(input())
    if n == 0:
        break
    sales = {}
    order = []
    for _ in range(n):
        i, p, q = input().split()
        p, q = int(p), int(q)
        if i not in sales:
            sales[i] = 0
            order.append(i)
        sales[i] += p * q
    res = [eid for eid in order if sales[eid] >= 1000000]
    if res:
        print('\n'.join(res))
    else:
        print("NA")