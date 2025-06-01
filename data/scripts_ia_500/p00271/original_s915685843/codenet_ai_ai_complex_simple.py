from functools import reduce
import operator
import sys
import itertools

def input_generator():
    while True:
        yield sys.stdin.readline()

def parse_line(line):
    try:
        nums = list(itertools.islice(map(int, line.strip().split()), 2))
        if len(nums) != 2:
            raise ValueError("Not two integers")
        return nums
    except:
        raise

def diff(a_b):
    return reduce(operator.sub, a_b)

gen = input_generator()
while True:
    try:
        line = next(gen)
        pair = parse_line(line)
        print(diff(pair))
    except (StopIteration, ValueError):
        break