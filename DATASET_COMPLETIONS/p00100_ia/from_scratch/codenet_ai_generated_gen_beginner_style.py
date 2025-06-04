while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    sales = {}
    order = []
    for _ in range(n):
        line = input().split()
        i = line[0]
        p = int(line[1])
        q = int(line[2])
        if i not in sales:
            sales[i] = 0
            order.append(i)
        sales[i] += p * q
    result = []
    for i in order:
        if sales[i] >= 1000000:
            result.append(i)
    if len(result) == 0:
        print("NA")
    else:
        for r in result:
            print(r)