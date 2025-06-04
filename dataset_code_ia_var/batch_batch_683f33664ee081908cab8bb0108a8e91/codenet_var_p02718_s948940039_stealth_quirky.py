from functools import reduce

get = lambda: list(map(int, input().split()))
n, m = get()
arr = get()
total = reduce(lambda x, y: x + y, arr)
f = lambda x: x * 4 * m >= total
res = [*filter(f, arr)]
print(["No", "Yes"][len(res) >= m])