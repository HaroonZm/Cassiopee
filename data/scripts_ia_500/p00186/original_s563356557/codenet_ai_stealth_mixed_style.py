def binary_search(qty, budg, price_aizu, price_reg, limit_aizu):
    from math import floor

    if budg < (qty - 1) * price_reg + price_aizu:
        return None

    if price_aizu * qty <= budg:
        a_count = budg // price_aizu
        a_count = min(a_count, limit_aizu)
        rest_money = budg - a_count * price_aizu
        r_count = rest_money // price_reg
        return (a_count, r_count)

    if price_aizu * limit_aizu + price_reg * (qty - limit_aizu) < budg:
        rest_money = budg - price_aizu * limit_aizu
        return (limit_aizu, rest_money // price_reg)

    a_count = limit_aizu // 2
    r_count = qty - a_count
    step = a_count // 2 + 1
    max_combo = (0, qty)

    while step > 0:
        cost = a_count * price_aizu + r_count * price_reg
        if cost <= budg:
            max_combo = (a_count, r_count)
            a_count += step + 1
            r_count -= step + 1
        else:
            a_count -= step + 1
            r_count += step + 1
        step //= 2

    return max_combo

def main():
    while True:
        try:
            line = input()
            if line.strip() == "0":
                break
            parts = list(map(int, line.split()))
            qty, budg, price_aizu, price_reg, limit_aizu = parts[0], parts[1], parts[2], parts[3], parts[4]

            res = binary_search(qty, budg, price_aizu, price_reg, limit_aizu)
            if res is not None:
                print(res[0], res[1])
            else:
                print("NA")
        except EOFError:
            break

if __name__ == "__main__":
    main()