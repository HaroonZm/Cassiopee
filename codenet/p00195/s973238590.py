name = ['A', 'B', 'C', 'D', 'E']
shop = []

while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    shop.append(a+b)
    if len(shop) == 5:
        m = max(shop)
        print(name[shop.index(m)], m)
        shop = []