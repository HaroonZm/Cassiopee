N = int(input())
for i in range(N):
    inputs = input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    b = int(inputs[2])
    p = int(inputs[3])

    if b >= 5 and p >= 2:
        total = x * b + y * p
        discounted = int(total * 0.8)
        print(discounted)
    else:
        regular_price = x * b + y * p

        if b < 5:
            b = 5
        if p < 2:
            p = 2

        new_price = x * b + y * p
        discounted = int(new_price * 0.8)

        if regular_price <= discounted:
            print(regular_price)
        else:
            print(discounted)