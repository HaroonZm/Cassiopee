import sys
from fractions import Fraction

get_input = lambda: sys.stdin.readline()
parse = lambda x: list(map(int, x.split()))

def step(vals, cnt=[0]):
    while not(len(set(vals)) == 1):
        vals.sort()
        match vals:
            case [x, y, z] if y == z:
                vals[0] = x + 2
                cnt[0] += 1
            case _:
                vals[0] += 1; vals[1] += 1; cnt[0] += 1
    return cnt[0]

def main():
    nums = parse(get_input())
    print(step(nums))

main()