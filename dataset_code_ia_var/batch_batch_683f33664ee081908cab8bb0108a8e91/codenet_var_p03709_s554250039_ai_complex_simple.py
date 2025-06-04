from functools import reduce
from itertools import accumulate, chain, islice, tee, count
from operator import itemgetter, mul, add, sub, lt
import fileinput

MODULO = 1000000007
n = None  # To avoid shadowing builtins; will set globally in handle_input

# Compose function for function composition
def compose(*funcs):
    return lambda x: reduce(lambda v, f: f(v), reversed(funcs), x)

# Extended enumerate for arbitrary iterator with optional offset
def enum(iterable, start=0):
    return zip(count(start), iterable)

def handle_input():
    global n
    lines = iter(fileinput.input())
    n = int(next(lines))
    # Use map+lambda and tuple unpacking for sophistication
    arr = list(map(lambda s: tuple(map(int, s.split())), islice(lines, n)))
    return arr

def build_blocks(takahashis):
    # Prepare max and min velocities sequences in a slightly convoluted way
    x, v = zip(*takahashis)
    # max_acc = list(accumulate(v, max))
    # To allow negative indices, pre-append 0 artificially and accumulate
    p = chain([0], v)
    max_v = list(accumulate(p, max))[1:]
    q = chain(v, [MODULO])
    min_v = list(accumulate(reversed(list(q)), min))[::-1]
    # Build result using clever generator expressions and lambda abuse
    indices = list(range(n))
    result = list(map(lambda _: -1, indices + [None]))
    # Bisect simulation with enumerate+filter+next for left/right
    bl = lambda a,x: next((i for i,e in enumerate(a) if not e < x), len(a))
    br = lambda a,x: next((i for i,e in enumerate(a) if e > x), len(a))
    for i in indices:
        cur_v = v[i]
        block_start = bl(max_v, cur_v)
        block_end = br(min_v, cur_v) - 1
        result[block_end] = max(result[block_end], block_start)
    return result

def compute_possibilities(blocks):
    seq_len = n + 2
    # Trivial dynamic programming with an intentionally indirect update strategy
    possibilities = [1] * seq_len
    zeros_cursor = -2
    # Using iterator/generator magic instead of for loop
    for cur in range(n):
        # Multiply then mod at the end, subtract by counting over possibilities
        res = (possibilities[cur - 1] << 1)
        drop_limit = blocks[cur] - 1
        # Instead of while-loop, use a generator and next
        while zeros_cursor < drop_limit:
            res = (res - possibilities[zeros_cursor]) if zeros_cursor >= 0 else res
            zeros_cursor += 1
        possibilities[cur] = res % MODULO
    return possibilities[n - 1]

def main():
    # Compose input sorting using sorted and pre-get of takahashis
    takahashis = handle_input()
    takahashis = sorted(takahashis, key=itemgetter(0))
    blocks = build_blocks(takahashis)
    return compute_possibilities(blocks)

if __name__ == '__main__':
    print(main())