import sys


def calculate_price(pack_count, unit_price, units_per_pack, discount_rate):
    
    full_packs = pack_count // units_per_pack
    leftover_units = pack_count % units_per_pack
    
    price_full_packs = full_packs * units_per_pack * unit_price * (1.0 - discount_rate)
    price_leftover_units = leftover_units * unit_price
    
    total_price = price_full_packs + price_leftover_units
    
    return total_price



def solve():
    
    while True:
        
        requested_weight = int(sys.stdin.readline())
        
        if requested_weight == 0:
            return
        
        # Initialize minimum price with a large value: the max price of the three options if bought without discount
        minimum_price = max([380*25, 550*17, 850*10])
        
        max_pack_a = requested_weight // 200
        
        for pack_a_count in range(max_pack_a + 1):
            
            remaining_weight_after_a = requested_weight - (pack_a_count * 200)
            
            max_pack_b = remaining_weight_after_a // 300
            
            for pack_b_count in range(max_pack_b + 1):
                
                remaining_weight_after_b = remaining_weight_after_a - (pack_b_count * 300)
                
                if remaining_weight_after_b % 500 != 0:
                    continue
                
                pack_c_count = remaining_weight_after_b // 500
                
                price_pack_a = calculate_price(pack_a_count, 380, 5, 0.20)
                price_pack_b = calculate_price(pack_b_count, 550, 4, 0.15)
                price_pack_c = calculate_price(pack_c_count, 850, 3, 0.12)
                
                total_price = price_pack_a + price_pack_b + price_pack_c
                
                if total_price < minimum_price:
                    minimum_price = total_price
        
        print("{:.0f}".format(minimum_price))



solve()