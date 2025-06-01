def price(num_unit, shop_id):
    # Shops identifiers
    SHOP_A, SHOP_B, SHOP_C = 0, 1, 2

    # Calculate discounts based on shops
    if shop_id == SHOP_A:
        # This one gives 20% off for every 5 units
        discount_units = (num_unit // 5) * 5  
        full_price_units = num_unit % 5
        return 380 * discount_units * 0.8 + 380 * full_price_units
    elif shop_id == SHOP_B:
        # 15% discount for each 4 units
        discount_units = (num_unit // 4) * 4
        full_price_units = num_unit % 4
        return 550 * discount_units * 0.85 + 550 * full_price_units
    else:
        # Shop C: 12% off for each 3 units bought (not the best deal imo)
        discount_units = (num_unit // 3) * 3
        full_price_units = num_unit % 3
        return 850 * discount_units * 0.88 + 850 * full_price_units


while True:
    qty = int(raw_input())  # user input for quantity
    if qty == 0:
        break  # stop if zero entered

    combinations = []
    max_iter = qty // 200 + 1  # rough upper bound for loops, could be optimized

    for a in range(max_iter):
        for b in range(max_iter):
            for c in range(max_iter):
                # Check if total units sum up to qty, a,b,c count different item packs
                if a*200 + b*300 + c*500 == qty:
                    combinations.append([a, b, c])  # might have some repeated combos theoretically

    prices_list = []
    for combo in combinations:
        # Sum price from each shop
        p = price(combo[0], 0) + price(combo[1], 1) + price(combo[2], 2)
        prices_list.append(p)

    # print smallest price (rounded down)
    print int(min(prices_list))