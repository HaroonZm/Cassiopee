import sys
from functools import reduce
from itertools import count, islice, compress, starmap, product

def elaborate_substrings(sign, c):
    return list(
        filter(
            lambda idx: sign[idx] == c,
            range(len(sign))
        )
    )

def generate_gaps(sign, target, start):
    # produce all possible gaps where extracting skips reveals target
    for gap in count(1):
        segment = sign[start::gap]
        if len(segment) < len(target):
            break
        yield gap

def found_target(sign, target):
    return any(
        any(
            (sign[st::gap][:len(target)] == target)
            for gap in generate_gaps(sign, target, st)
        )
        for st in elaborate_substrings(sign, target[0])
    )

def solve(target_name, n):
    total = 0
    board_iter = (input() for _ in range(n))
    vectorized_result = map(lambda sb: found_target(sb, target_name), board_iter)
    total = reduce(lambda x, y: x + y, vectorized_result, 0)
    return total

def main(args):
    n = int(input())
    s = input()
    res = solve(s, n)
    print(res)

if __name__ == '__main__':
    main(sys.argv[1:])