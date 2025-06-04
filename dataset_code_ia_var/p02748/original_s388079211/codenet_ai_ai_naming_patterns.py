input_vals = input().split(" ")
num_A, num_B, num_coupons = [int(input_vals[idx]) for idx in range(3)]

list_A = [int(val) for val in input().split(" ")]
list_B = [int(val) for val in input().split(" ")]

coupon_list = []
for idx_coupon in range(num_coupons):
    coupon_vals = [int(val) for val in input().split(" ")]
    coupon_list.append(coupon_vals)

min_total_price = min(list_A) + min(list_B)
for coupon in coupon_list:
    idx_A, idx_B, discount = coupon
    coupon_price = list_A[idx_A - 1] + list_B[idx_B - 1] - discount
    if coupon_price < min_total_price:
        min_total_price = coupon_price

print(min_total_price)