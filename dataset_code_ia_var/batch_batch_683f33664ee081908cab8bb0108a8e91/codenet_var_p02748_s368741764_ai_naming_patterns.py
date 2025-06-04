num_type_a, num_type_b, num_coupon = map(int, input().split())
price_type_a_list = list(map(int, input().split()))
price_type_b_list = list(map(int, input().split()))
coupon_info_list = [list(map(int, input().split())) for _ in range(num_coupon)]

min_price_no_coupon = min(price_type_a_list) + min(price_type_b_list)
price_combo_with_coupon_list = [
    price_type_a_list[coupon_a_idx-1] + price_type_b_list[coupon_b_idx-1] - coupon_discount
    for coupon_a_idx, coupon_b_idx, coupon_discount in coupon_info_list
]
min_price_with_coupon = min(price_combo_with_coupon_list) if price_combo_with_coupon_list else float('inf')
print(min(min_price_no_coupon, min_price_with_coupon))