def calc_cost(amount, bag_size, unit_price, discount_unit, discount_rate):
    bags = amount // bag_size
    discounted_groups = bags // discount_unit
    remainder = bags % discount_unit
    cost = (unit_price * discount_unit * discounted_groups) * (1 - discount_rate) + unit_price * remainder
    return cost

def main():
    shops = [
        (200, 380, 5, 0.20),  # Shop A
        (300, 550, 4, 0.15),  # Shop B
        (500, 850, 3, 0.12),  # Shop C
    ]

    while True:
        a = int(input())
        if a == 0:
            break

        min_cost = float('inf')
        for bag_size, unit_price, discount_unit, discount_rate in shops:
            if a % bag_size == 0:
                cost = calc_cost(a, bag_size, unit_price, discount_unit, discount_rate)
                if cost < min_cost:
                    min_cost = cost

        print(int(min_cost))

if __name__ == '__main__':
    main()