number_of_test_cases = int(input())

for test_case_index in range(number_of_test_cases):

    price_per_bread, price_per_pastry, number_of_breads, number_of_pastries = map(int, input().split())

    total_regular_price = price_per_bread * number_of_breads + price_per_pastry * number_of_pastries

    minimum_bread_required_for_discount = 5
    minimum_pastry_required_for_discount = 2

    if number_of_breads >= minimum_bread_required_for_discount and number_of_pastries >= minimum_pastry_required_for_discount:
        total_discounted_price = int((price_per_bread * number_of_breads + price_per_pastry * number_of_pastries) * 0.8)
        print(total_discounted_price)
    else:
        adjusted_bread_count = max(number_of_breads, minimum_bread_required_for_discount)
        adjusted_pastry_count = max(number_of_pastries, minimum_pastry_required_for_discount)
        total_discounted_price = int((price_per_bread * adjusted_bread_count + price_per_pastry * adjusted_pastry_count) * 0.8)

        if total_regular_price <= total_discounted_price:
            print(total_regular_price)
        else:
            print(total_discounted_price)