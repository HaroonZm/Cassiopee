from functools import reduce
print(reduce(lambda acc, _: acc + int(input()), range(10), 0))