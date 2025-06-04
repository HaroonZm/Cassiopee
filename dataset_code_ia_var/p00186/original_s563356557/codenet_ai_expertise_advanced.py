from sys import stdin

def binary_search(quantity, budget, aizu_chicken_price, chicken_price, aizu_chicken_limit):
    # Impossible minimum: 1 aizu + (quantity-1) normal
    if budget < (quantity - 1) * chicken_price + aizu_chicken_price:
        return None

    # All Aizu possible?
    max_aizu = min(aizu_chicken_limit, budget // aizu_chicken_price, quantity)
    if max_aizu == quantity and aizu_chicken_price * quantity <= budget:
        return quantity, 0

    # All Aizu up to limit, rest normal
    if aizu_chicken_price * aizu_chicken_limit + chicken_price * (quantity - aizu_chicken_limit) <= budget:
        rest = budget - aizu_chicken_price * aizu_chicken_limit
        chicken_count = min(quantity - aizu_chicken_limit, rest // chicken_price)
        return aizu_chicken_limit, chicken_count

    # Binary search over possible count of Aizu chickens
    lo, hi = 0, min(aizu_chicken_limit, quantity)
    best = None
    while lo <= hi:
        mid = (lo + hi) // 2
        normal = quantity - mid
        cost = mid * aizu_chicken_price + normal * chicken_price
        if cost <= budget:
            best = (mid, normal)
            lo = mid + 1
        else:
            hi = mid - 1
    return best

def parse_input():
    for line in stdin:
        line = line.strip()
        if line == "0":
            break
        yield map(int, line.split())

def main():
    for data in parse_input():
        quantity, budget, aizu_chicken_price, chicken_price, aizu_chicken_limit = data
        result = binary_search(quantity, budget, aizu_chicken_price, chicken_price, aizu_chicken_limit)
        print(f"{result[0]} {result[1]}" if result else "NA")

if __name__ == "__main__":
    main()