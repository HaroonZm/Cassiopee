from functools import reduce

def g(_): return list(map(int, _.split()))
x, y, z = reduce(lambda p, q: p + [q], g(input()), [])[0:3]
result = {True: "Yes", False: "No"}[(x + y) >= z]
print(result)