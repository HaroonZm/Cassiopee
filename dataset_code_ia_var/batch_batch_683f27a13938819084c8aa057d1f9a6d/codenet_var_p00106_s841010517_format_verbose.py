import sys

def calculate_price(
    number_of_packs,
    price_per_pack,
    units_per_pack,
    discount_rate
):
    discounted_units = (number_of_packs // units_per_pack) * units_per_pack
    discounted_price = discounted_units * price_per_pack * (1.0 - discount_rate)
    non_discounted_units = number_of_packs % units_per_pack
    non_discounted_price = non_discounted_units * price_per_pack
    total_price = discounted_price + non_discounted_price
    return total_price

def solve():
    while True:
        required_weight_grams = int(sys.stdin.readline())
        if required_weight_grams == 0:
            return
        
        minimum_total_cost = max([380 * 25, 550 * 17, 850 * 10])
        
        for two_hundred_gram_packs in range(0, required_weight_grams // 200 + 1):
            remaining_weight_after_200 = required_weight_grams - two_hundred_gram_packs * 200
            
            for three_hundred_gram_packs in range(0, remaining_weight_after_200 // 300 + 1):
                remaining_weight_after_300 = remaining_weight_after_200 - three_hundred_gram_packs * 300
                
                if remaining_weight_after_300 % 500 != 0:
                    continue
                
                five_hundred_gram_packs = remaining_weight_after_300 // 500
                
                total_cost = (
                    calculate_price(two_hundred_gram_packs, 380, 5, 0.2) +
                    calculate_price(three_hundred_gram_packs, 550, 4, 0.15) +
                    calculate_price(five_hundred_gram_packs, 850, 3, 0.12)
                )
                
                if total_cost < minimum_total_cost:
                    minimum_total_cost = total_cost
        
        print("{:.0f}".format(minimum_total_cost))

solve()