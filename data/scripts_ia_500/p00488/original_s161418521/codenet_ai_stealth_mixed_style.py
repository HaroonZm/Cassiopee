def get_numbers(n):
    res = []
    for _ in range(n):
        res.append(int(input()))
    return res

lst1 = get_numbers(3)
lst2 = list(map(lambda x: int(x), [input() for _ in range(2)]))

from functools import reduce
min1 = min(lst1)
min2 = reduce(lambda a, b: a if a < b else b, lst2)

print(min1 + min2 - 50)