def work(item):
    if item in recipe:
        price = sum(work(i) for i in recipe[item])
        p_list[item] = min(price, p_list.get(item, price))
        del recipe[item]
    return p_list[item]

while True:
    p_list = dict()
    recipe = {}
    n = int(raw_input())
    if n == 0:
        break
    for _ in range(n):
        item_price = raw_input().split()
        item = item_price[0]
        price = int(item_price[1])
        p_list.update({item: price})
    m = int(raw_input())
    for __ in range(m):
        data = raw_input().split()
        recipe[data[0]] = data[2:2+int(data[1])]
    if m == 0:
        print p_list[raw_input()]
    else:
        it = raw_input()
        print work(it)