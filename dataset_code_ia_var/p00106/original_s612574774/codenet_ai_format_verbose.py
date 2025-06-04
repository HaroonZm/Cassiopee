def calculate_minimum_cost(total_weight):
    
    minimum_cost = 1e9

    # Iterate over possible number of 500g packs
    for num_500g_packs in range(total_weight // 500 + 1):
        
        remaining_weight_after_500g = total_weight - num_500g_packs * 500

        # Iterate over possible number of 300g packs
        for num_300g_packs in range(remaining_weight_after_500g // 300 + 1):
            
            remaining_weight_after_300g = remaining_weight_after_500g - num_300g_packs * 300
            
            # Check if remaining weight can be exactly filled with 200g packs
            if remaining_weight_after_300g % 200 == 0:
                num_200g_packs = remaining_weight_after_300g // 200
                pack_counts = [num_200g_packs, num_300g_packs, num_500g_packs]
                batch_cost = compute_batch_cost(pack_counts)
                minimum_cost = min(minimum_cost, batch_cost)
    
    return minimum_cost

def compute_batch_cost(pack_counts):
    
    base_prices = [380, 550, 850]
    discount_rates = [0.2, 0.15, 0.12]
    discount_thresholds = [5, 4, 3]

    total_cost = 0

    for pack_index in [0, 1, 2]:
        number_of_packs = pack_counts[pack_index]
        price_per_pack = base_prices[pack_index]
        discount_rate = discount_rates[pack_index]
        threshold = discount_thresholds[pack_index]

        discounted_packs = (number_of_packs // threshold) * threshold
        full_price_packs = number_of_packs - discounted_packs

        cost_for_type = price_per_pack * (
            full_price_packs + discounted_packs * (1 - discount_rate)
        )
        total_cost += cost_for_type

    return total_cost

while True:
    
    user_input_weight = input()
    
    if user_input_weight == 0:
        break

    minimum_total_cost = calculate_minimum_cost(user_input_weight)
    print(int(minimum_total_cost))