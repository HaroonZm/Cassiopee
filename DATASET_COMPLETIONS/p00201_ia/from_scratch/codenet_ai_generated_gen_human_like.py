while True:
    n = int(input())
    if n == 0:
        break

    price = {}
    for _ in range(n):
        s, p = input().split()
        price[s] = int(p)

    m = int(input())
    recipes = {}
    for _ in range(m):
        parts = input().split()
        o = parts[0]
        k = int(parts[1])
        ingredients = parts[2:]
        recipes[o] = ingredients

    target = input()

    from functools import lru_cache

    @lru_cache(None)
    def dfs(item):
        if item not in recipes:
            return price[item]
        cost_make = 0
        for ingr in recipes[item]:
            cost_make += dfs(ingr)
        return min(price[item], cost_make)

    print(dfs(target))