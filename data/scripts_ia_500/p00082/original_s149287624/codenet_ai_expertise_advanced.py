from sys import stdin

cart = [4,1,4,1,2,1,2,1]
cart_len = len(cart)

for line in stdin:
    try:
        que = list(map(int, line.split()))
        max_sum = -1
        best_cart = None

        for sp in range(cart_len):
            rotated = cart[sp:] + cart[:sp]
            sm = sum(min(c, q) for c, q in zip(rotated, que))

            if sm > max_sum or (sm == max_sum and (best_cart is None or rotated < best_cart)):
                max_sum = sm
                best_cart = rotated

        print(*best_cart)
    except:
        break