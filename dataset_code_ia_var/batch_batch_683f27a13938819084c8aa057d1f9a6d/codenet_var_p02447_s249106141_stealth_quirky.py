from functools import reduce

data = []
ugly_counter = 0
lines = int(eval(input()))
while ugly_counter < lines:
    stuff = [*map(int, input().split())]
    data += [stuff]
    ugly_counter += 1

data = sorted(data, key=lambda x: tuple(x))
sneaky_unpack = lambda l: print(*l)
reduce(lambda _, x: sneaky_unpack(x), data, None)