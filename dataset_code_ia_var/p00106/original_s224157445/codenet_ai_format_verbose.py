def calculate_total_price_per_unit_shop(number_of_units, shop_index):

    SHOP_A_INDEX = 0
    SHOP_B_INDEX = 1
    SHOP_C_INDEX = 2

    if shop_index == SHOP_A_INDEX:
        units_with_discount = (number_of_units // 5) * 5
        discounted_price = 380 * units_with_discount * 0.8
        non_discounted_units = number_of_units % 5
        non_discounted_price = 380 * non_discounted_units
        return discounted_price + non_discounted_price

    elif shop_index == SHOP_B_INDEX:
        units_with_discount = (number_of_units // 4) * 4
        discounted_price = 550 * units_with_discount * 0.85
        non_discounted_units = number_of_units % 4
        non_discounted_price = 550 * non_discounted_units
        return discounted_price + non_discounted_price

    else:  # SHOP_C_INDEX
        units_with_discount = (number_of_units // 3) * 3
        discounted_price = 850 * units_with_discount * 0.88
        non_discounted_units = number_of_units % 3
        non_discounted_price = 850 * non_discounted_units
        return discounted_price + non_discounted_price


while True:

    total_quantity = int(raw_input())

    if total_quantity == 0:
        break

    valid_combinations = []

    max_possible_units_shop_a = total_quantity // 200
    max_possible_units_shop_b = total_quantity // 300
    max_possible_units_shop_c = total_quantity // 500

    for units_shop_a in range(max_possible_units_shop_a + 1):

        for units_shop_b in range(max_possible_units_shop_b + 1):

            for units_shop_c in range(max_possible_units_shop_c + 1):

                combined_quantity = (
                    units_shop_a * 200 +
                    units_shop_b * 300 +
                    units_shop_c * 500
                )

                if combined_quantity == total_quantity:
                    valid_combinations.append(
                        [units_shop_a, units_shop_b, units_shop_c]
                    )

    total_prices_for_combinations = []

    for current_combination in valid_combinations:

        price_shop_a = calculate_total_price_per_unit_shop(current_combination[0], 0)
        price_shop_b = calculate_total_price_per_unit_shop(current_combination[1], 1)
        price_shop_c = calculate_total_price_per_unit_shop(current_combination[2], 2)

        total_price = price_shop_a + price_shop_b + price_shop_c

        total_prices_for_combinations.append(total_price)

    minimum_total_price = min(total_prices_for_combinations)

    print int(minimum_total_price)