def calculate_minimal_remaining_amount():
    number_of_items, initial_total, coefficient_a, coefficient_b, multiplier_p, multiplier_q = map(int, input().split())

    if coefficient_a == 1 and coefficient_b == 1:
        total_cost_per_item = multiplier_p + multiplier_q
        total_purchase_cost = total_cost_per_item * number_of_items

        if total_purchase_cost <= initial_total:
            return initial_total - total_purchase_cost
        else:
            max_full_purchases = initial_total // total_cost_per_item
            minimal_difference = min(
                initial_total - max_full_purchases * total_cost_per_item,
                (max_full_purchases + 1) * total_cost_per_item - initial_total
            )
            return minimal_difference

    else:
        minimal_remaining_amount = initial_total
        maximum_exponent_to_check = min(number_of_items - 1, 40)

        for purchase_index in range(maximum_exponent_to_check, -1, -1):
            current_purchase_cost = multiplier_p * (coefficient_a ** purchase_index) + multiplier_q * (coefficient_b ** purchase_index)

            if initial_total < current_purchase_cost:
                minimal_remaining_amount = min(minimal_remaining_amount, current_purchase_cost - initial_total)
            else:
                initial_total -= current_purchase_cost

            minimal_remaining_amount = min(minimal_remaining_amount, initial_total)

        return minimal_remaining_amount

def main():
    print(calculate_minimal_remaining_amount())

if __name__ == '__main__':
    main()