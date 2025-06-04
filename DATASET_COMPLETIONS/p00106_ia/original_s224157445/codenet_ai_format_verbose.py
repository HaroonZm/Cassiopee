def calculate_price(number_of_units, shop_identifier):
    
    SHOP_A = 0
    SHOP_B = 1
    SHOP_C = 2
    
    if shop_identifier == SHOP_A:
        discount_units = (number_of_units // 5) * 5
        price_per_unit = 380
        discount_rate = 0.8
        discounted_price = price_per_unit * discount_units * discount_rate
        full_price_units = number_of_units % 5
        full_price = price_per_unit * full_price_units
        total_price = discounted_price + full_price
        return total_price

    elif shop_identifier == SHOP_B:
        discount_units = (number_of_units // 4) * 4
        price_per_unit = 550
        discount_rate = 0.85
        discounted_price = price_per_unit * discount_units * discount_rate
        full_price_units = number_of_units % 4
        full_price = price_per_unit * full_price_units
        total_price = discounted_price + full_price
        return total_price

    else:
        discount_units = (number_of_units // 3) * 3
        price_per_unit = 850
        discount_rate = 0.88
        discounted_price = price_per_unit * discount_units * discount_rate
        full_price_units = number_of_units % 3
        full_price = price_per_unit * full_price_units
        total_price = discounted_price + full_price
        return total_price


while True:
    
    quantity_required = int(raw_input())
    
    if quantity_required == 0:
        break

    possible_combinations = []
    
    max_a_units = quantity_required // 200 + 1
    max_b_units = quantity_required // 200 + 1
    max_c_units = quantity_required // 200 + 1
    
    for units_a in range(max_a_units):
        for units_b in range(max_b_units):
            for units_c in range(max_c_units):
                
                total_units = units_a * 200 + units_b * 300 + units_c * 500
                
                if total_units == quantity_required:
                    possible_combinations.append([units_a, units_b, units_c])

    calculated_prices = []
    
    for combination in possible_combinations:
        
        price_a = calculate_price(combination[0], 0)
        price_b = calculate_price(combination[1], 1)
        price_c = calculate_price(combination[2], 2)
        
        total_combination_price = price_a + price_b + price_c
        
        calculated_prices.append(total_combination_price)

    print int(min(calculated_prices))