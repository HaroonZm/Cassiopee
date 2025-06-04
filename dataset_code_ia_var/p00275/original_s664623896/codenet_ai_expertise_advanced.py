from sys import stdin
from itertools import cycle, islice

def process_input():
    lines = iter(stdin)
    while True:
        try:
            n = int(next(lines))
            if n == 0:
                break
            s = next(lines).strip()
            ba = 0
            p = [0] * n
            get_index = cycle(range(n))
            for i, (ch, idx) in enumerate(zip(s, islice(get_index, 100))):
                match ch:
                    case 'M':
                        p[idx] += 1
                    case 'L':
                        p[idx] += ba + 1
                        ba = 0
                    case _:
                        ba += p[idx] + 1
                        p[idx] = 0
            print(*sorted(p), ba)
        except StopIteration:
            break

process_input()