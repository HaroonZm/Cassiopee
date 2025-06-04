val_a, val_b, val_c, val_d = map(int, input().split())
parity_product_ab = (val_a * val_b) % 2
parity_sum_cd = (val_c + val_d) % 2
is_both_odd = parity_product_ab * parity_sum_cd == 1
print("No" if is_both_odd else "Yes")