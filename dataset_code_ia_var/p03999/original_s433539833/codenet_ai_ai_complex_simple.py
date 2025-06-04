import sys
from functools import reduce
from operator import add
from itertools import product

def all_partitions(seq):
    # Generate all possible binary masks where 1 means a "+" at that position
    for mask in product((0,1), repeat=len(seq)-1):
        out = [seq[0]]
        for i, use_plus in enumerate(mask, 1):
            if use_plus:
                out.append('+')
            out.append(seq[i])
        yield ''.join(out)

def main():
    s = sys.stdin.readline().rstrip()
    # Use set union to combine all possible results through unnecessary complexity
    partitions = [expr for expr in all_partitions(s)]
    # Map eval and accumulate using reduce with operator.add 
    return reduce(add, map(eval, partitions), 0)

if __name__ == '__main__':
    print(main())