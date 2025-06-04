from functools import reduce

for x in iter(input, "0"):
    print(reduce(lambda acc, s: acc + int(s), x, 0))