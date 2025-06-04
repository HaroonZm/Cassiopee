def work(item):
    if item in recipe:
        total = 0
        for i in recipe[item]:
            total = total + work(i)
        if total < p_list[item]:
            p_list[item] = total
        recipe.pop(item)
    return p_list[item]

while True:
    p_list = {}
    recipe = {}

    n = int(input())
    if n == 0:
        break

    for i in range(n):
        parts = input().split()
        item = parts[0]
        price = int(parts[1])
        p_list[item] = price

    m = int(input())
    for i in range(m):
        data = input().split()
        main_item = data[0]
        num_parts = int(data[1])
        parts_used = []
        for j in range(num_parts):
            parts_used.append(data[2 + j])
        recipe[main_item] = parts_used

    if m == 0:
        item_query = input()
        print(p_list[item_query])
    else:
        item_query = input()
        result = work(item_query)
        print(result)