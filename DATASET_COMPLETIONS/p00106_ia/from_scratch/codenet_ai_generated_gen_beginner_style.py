while True:
    a = int(input())
    if a == 0:
        break

    # Shop data: (amount_per_bag, price_per_bag, pack_size_for_discount, discount_rate)
    shops = [
        (200, 380, 5, 0.20),
        (300, 550, 4, 0.15),
        (500, 850, 3, 0.12),
    ]

    min_cost = 10**9

    # Try all combinations of bags from shop A, B, C
    # Since amount max is 5000g and minimum bag is 200g,
    # max bags per shop won't be large, so brute force is ok.
    max_a = a // shops[0][0] + 1
    max_b = a // shops[1][0] + 1
    max_c = a // shops[2][0] + 1

    for na in range(max_a):
        for nb in range(max_b):
            for nc in range(max_c):
                total_amount = na * shops[0][0] + nb * shops[1][0] + nc * shops[2][0]
                if total_amount == a:
                    cost = 0
                    # Shop A cost
                    pack = shops[0][2]
                    disc = shops[0][3]
                    full_pack_num = na // pack
                    rem = na % pack
                    cost += int(((shops[0][1] * pack) * (1 - disc)) * full_pack_num + shops[0][1] * rem)

                    # Shop B cost
                    pack = shops[1][2]
                    disc = shops[1][3]
                    full_pack_num = nb // pack
                    rem = nb % pack
                    cost += int(((shops[1][1] * pack) * (1 - disc)) * full_pack_num + shops[1][1] * rem)

                    # Shop C cost
                    pack = shops[2][2]
                    disc = shops[2][3]
                    full_pack_num = nc // pack
                    rem = nc % pack
                    cost += int(((shops[2][1] * pack) * (1 - disc)) * full_pack_num + shops[2][1] * rem)

                    if cost < min_cost:
                        min_cost = cost

    print(min_cost)