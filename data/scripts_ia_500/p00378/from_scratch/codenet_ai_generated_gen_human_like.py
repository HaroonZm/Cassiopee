A, B, X = map(int, input().split())

# Convert X from milliliters to number of 0.5 liter units (each 500 ml)
units = (X + 499) // 500  # ceil division to cover at least X ml

min_price = float('inf')
for one_liter_bottles in range(units // 2 + 2):  # up to one more than max possible
    half_liter_bottles = max(0, units - 2 * one_liter_bottles)
    price = one_liter_bottles * A + half_liter_bottles * B
    if price < min_price and (one_liter_bottles * 1000 + half_liter_bottles * 500) >= X:
        min_price = price

print(min_price)