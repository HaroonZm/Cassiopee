def calc_after_tax(p, rate):
    return (p * (100 + rate) + 50) // 100

while True:
    x, y, s = map(int, input().split())
    if x == 0 and y == 0 and s == 0:
        break
    max_price = 0
    for a in range(1, s):
        b = s - a
        # check all pairs that sum to s at VAT rate x
        if calc_after_tax(a, x) + calc_after_tax(b, x) == s:
            price = calc_after_tax(a, y) + calc_after_tax(b, y)
            if price > max_price:
                max_price = price
    print(max_price)