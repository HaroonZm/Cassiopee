n = int(input())
orders = {}
for _ in range(n):
    product, count = input().split()
    count = int(count)
    if product in orders:
        orders[product] += count
    else:
        orders[product] = count

sorted_products = sorted(orders.keys(), key=lambda x: (len(x), x))

for product in sorted_products:
    print(product, orders[product])