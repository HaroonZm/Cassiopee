while True:
    a = int(input())
    if a == 0:
        break

    # Shop info: amount per bag, unit price, discounted units, discount rate
    shops = [
        (200, 380, 5, 0.20),
        (300, 550, 4, 0.15),
        (500, 850, 3, 0.12)
    ]

    # Since amount a is at most 5000, max bags needed per shop is a // min amount + 1 for safety
    max_bags = [a // s[0] + 1 for s in shops]

    # Initialize minimum cost with a large number
    min_cost = 10**9

    # Try all combinations of bags from shops A, B, and C
    for i in range(max_bags[0] + 1):
        for j in range(max_bags[1] + 1):
            for k in range(max_bags[2] + 1):
                total_amount = i * shops[0][0] + j * shops[1][0] + k * shops[2][0]
                if total_amount == a:
                    cost = 0
                    # Calculate cost for shop A
                    if i > 0:
                        d_unit = shops[0][2]
                        d_rate = shops[0][3]
                        group = i // d_unit
                        remain = i % d_unit
                        cost += (group * d_unit * shops[0][1]) * (1 - d_rate) + remain * shops[0][1]
                    # Calculate cost for shop B
                    if j > 0:
                        d_unit = shops[1][2]
                        d_rate = shops[1][3]
                        group = j // d_unit
                        remain = j % d_unit
                        cost += (group * d_unit * shops[1][1]) * (1 - d_rate) + remain * shops[1][1]
                    # Calculate cost for shop C
                    if k > 0:
                        d_unit = shops[2][2]
                        d_rate = shops[2][3]
                        group = k // d_unit
                        remain = k % d_unit
                        cost += (group * d_unit * shops[2][1]) * (1 - d_rate) + remain * shops[2][1]

                    if cost < min_cost:
                        min_cost = cost

    print(int(min_cost))