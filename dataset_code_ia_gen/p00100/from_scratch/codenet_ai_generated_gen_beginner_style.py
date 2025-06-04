while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    sales = {}
    order = []
    for _ in range(n):
        data = input().split()
        i = data[0]
        p = int(data[1])
        q = int(data[2])
        if i not in sales:
            sales[i] = 0
            order.append(i)
        sales[i] += p * q
    result = []
    for i in order:
        if sales[i] >= 1000000:
            result.append(i)
    if result:
        for r in result:
            print(r)
    else:
        print("NA")