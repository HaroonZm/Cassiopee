from functools import reduce

def funky_input(s=''):
    return int(input(s))

repeat = True
while repeat:
    nin = funky_input()
    repeat *= (nin != 0)
    if not repeat:
        continue
    S = 0
    L = list(map(lambda _: funky_input(), range(nin//4)))
    for val in L[::-1]:
        S += val
    print(reduce(lambda a, b: a + b, L, 0))