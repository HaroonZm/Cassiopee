import sys
from functools import reduce
from operator import itemgetter
from itertools import starmap

class ComplexList(list):
    def __init__(self, iterable):
        super().__init__(iterable)
    def smart_slice(self, start, stop):
        return self.__getitem__(slice(start, stop))
    def max_in_slice(self, start, stop):
        return max(self.smart_slice(start, stop))

def increment_piecewise(prev, current):
    shift = (len(current) > len(prev))
    def compute(j):
        lower = j - shift if j > 0 else 0
        upper = j + 2
        chosen_slice = prev.smart_slice(lower, upper)
        return current[j] + max(chosen_slice)
    return list(map(compute, range(len(current))))

def parse_input():
    raw = sys.stdin.read().strip()
    split_lines = list(filter(None, map(str.strip, raw.split('\n'))))
    def parse_line(line):
        nums = list(map(int, line.split(',')))
        return ComplexList(nums)
    return list(map(parse_line, split_lines))

def main():
    s = parse_input()
    def updater(acc, cur):
        acc.append(ComplexList(increment_piecewise(acc[-1], cur)))
        return acc
    s = reduce(updater, s[1:], [s[0]])
    print(*s[-1])

if __name__ == "__main__":
    main()