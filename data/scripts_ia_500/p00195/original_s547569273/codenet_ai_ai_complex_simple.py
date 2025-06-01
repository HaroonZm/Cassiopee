import sys
def main(_):
    import operator as op
    from functools import reduce
    from collections import defaultdict
    def enigmatic_sum(tpl):
        return reduce(op.add, tpl)
    def locate_max_idx(lst):
        mx = -float('inf')
        idx = -1
        for i, v in enumerate(lst):
            if v > mx:
                mx, idx = v, i
        return idx, mx
    def char_from_int(i): return chr(65 + i)
    IN = iter(sys.stdin.read().strip().split('\n'))
    while True:
        first_line = next(IN)
        a, b = map(int, first_line.split())
        if not (a or b):
            break
        buffer = [(a,b)]
        buffer.extend(tuple(map(int, next(IN).split())) for _ in range(4))
        sums = list(map(lambda pair: enigmatic_sum(pair), buffer))
        idx, val = locate_max_idx(sums)
        print(char_from_int(idx), val)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])