def price(num_unit, shop):
    A, B, C = 0, 1, 2
    
    if shop == A:
        num_discount = (num_unit / 5) * 5
        return 380 * num_discount * 0.8 + 380 * (num_unit % 5)
    elif shop == B:
        num_discount = (num_unit / 4) * 4
        return 550 * num_discount * 0.85 + 550 * (num_unit % 4)
    else:
        num_discount = (num_unit / 3) * 3
        return 850 * num_discount * 0.88 + 850 * (num_unit % 3)

while True:
    quantity = int(raw_input())
    if quantity == 0: break

    comb = []
    for a in range(quantity / 200 + 1):
        for b in range(quantity / 200 + 1):
            for c in range(quantity / 200 + 1):
                if a * 200 + b * 300 + c * 500 == quantity:
                    comb.append([a, b, c])

    prices = []
    for c in comb:
        prices.append(price(c[0], 0) + price(c[1], 1) + price(c[2], 2))

    print int(min(prices))