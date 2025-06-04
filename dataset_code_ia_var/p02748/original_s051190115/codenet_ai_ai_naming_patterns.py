num_person_a, num_person_b, num_coupons = map(int, input().split())
person_a_costs = list(map(int, input().split()))
person_b_costs = list(map(int, input().split()))

coupon_a_indices = []
coupon_b_indices = []
coupon_discounts = []

for coupon_idx in range(num_coupons):
    curr_a_idx, curr_b_idx, curr_discount = map(int, input().split())
    coupon_a_indices.append(curr_a_idx)
    coupon_b_indices.append(curr_b_idx)
    coupon_discounts.append(curr_discount)

min_total_without_coupon = min(person_a_costs) + min(person_b_costs)

coupon_totals = []
for coupon_idx in range(num_coupons):
    curr_a_total = person_a_costs[coupon_a_indices[coupon_idx] - 1]
    curr_b_total = person_b_costs[coupon_b_indices[coupon_idx] - 1]
    total_after_discount = curr_a_total + curr_b_total - coupon_discounts[coupon_idx]
    coupon_totals.append(total_after_discount)

min_total_with_coupon = min(coupon_totals) if coupon_totals else min_total_without_coupon

print(min(min_total_without_coupon, min_total_with_coupon))