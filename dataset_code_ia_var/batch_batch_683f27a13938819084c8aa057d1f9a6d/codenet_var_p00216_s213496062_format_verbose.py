def calculate_shipping_fee(package_weight):

    base_fee = 1150

    if package_weight <= 10:
        return base_fee

    remaining_weight = package_weight - 10

    if remaining_weight <= 10:
        return base_fee + 125 * remaining_weight

    base_fee += 1250
    remaining_weight -= 10

    if remaining_weight <= 10:
        return base_fee + 140 * remaining_weight

    base_fee += 1400
    remaining_weight -= 10

    return base_fee + 160 * remaining_weight


while True:

    user_input_weight = int(input())

    if user_input_weight == -1:
        break

    discount_amount = 4280 - calculate_shipping_fee(user_input_weight)

    print(discount_amount)