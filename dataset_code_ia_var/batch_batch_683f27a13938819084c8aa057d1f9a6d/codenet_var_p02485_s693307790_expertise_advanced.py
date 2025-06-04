from functools import reduce

def digit_sum():
    for x in iter(raw_input, '0'):
        print(reduce(lambda a, b: a + b, map(int, x)))

digit_sum()