while True:
    line = input()
    qua, bag = line.split()
    qua = int(qua)
    bag = int(bag)
    if qua == 0:
        break
    price = input().split()
    for i in range(qua):
        price[i] = int(price[i])
    price.sort(reverse=True)
    for i in range(qua):
        if (i + 1) % bag == 0:
            price[i] = -1
    count = 0
    while count < qua // bag:
        price.remove(-1)
        count += 1
    total = 0
    for p in price:
        total += p
    print(total)