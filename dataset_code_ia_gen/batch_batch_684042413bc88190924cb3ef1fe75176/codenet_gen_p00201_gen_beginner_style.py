while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    items_price = {}
    for _ in range(n):
        line = input().split()
        name = line[0]
        price = int(line[1])
        items_price[name] = price
    m = int(input())
    recipes = {}
    for _ in range(m):
        line = input().split()
        out_item = line[0]
        k = int(line[1])
        in_items = line[2:]
        recipes[out_item] = in_items

    target = input()

    # メモ化による再帰的な最小費用計算
    memo = {}
    def cost(item):
        if item in memo:
            return memo[item]
        # 買う場合の値段
        res = items_price[item]
        # 作る場合の値段
        if item in recipes:
            total = 0
            for in_item in recipes[item]:
                total += cost(in_item)
            if total < res:
                res = total
        memo[item] = res
        return res

    print(cost(target))