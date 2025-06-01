import sys
from functools import reduce
from operator import itemgetter

def super_map(f, data):
    return list(map(lambda x: list(map(f, x.split(','))), data))

def sliding_max(arr, idx, shift):
    left = max(0, idx+shift)
    right = min(len(arr), idx+shift+2)
    return max(arr[left:right])

def complex_enumerate(lst):
    return map(lambda x: x, enumerate(lst))

def fuse_max(prev_row, curr_row):
    k = len(curr_row)
    b = (k > len(prev_row)) and 1 or 0
    def compute(j):
        t = j - b
        start = max(0, (t if j > 0 else 0))
        end = min(len(prev_row), t+2)
        return curr_row[j] + max(prev_row[start:end])
    return list(map(compute, range(k)))

def main():
    s = super_map(int, sys.stdin)
    s = reduce(lambda acc, i: acc + [fuse_max(acc[-1], s[i])], range(1, len(s)), [s[0]])
    print(*s[-1])

main()