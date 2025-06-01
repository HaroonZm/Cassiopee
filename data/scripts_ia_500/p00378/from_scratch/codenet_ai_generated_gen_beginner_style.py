A, B, X = map(int, input().split())
min_price = 10**9
for one_liter_bottles in range(0, X // 1000 + 2):
    for half_liter_bottles in range(0, X // 500 + 2):
        total_ml = one_liter_bottles * 1000 + half_liter_bottles * 500
        if total_ml >= X:
            price = one_liter_bottles * A + half_liter_bottles * B
            if price < min_price:
                min_price = price
print(min_price)