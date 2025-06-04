from itertools import cycle
import sys

def process_input():
    lines = iter(sys.stdin.read().splitlines())
    while True:
        N_line = next(lines, None)
        if N_line is None:
            break
        N = int(N_line)
        if N == 0:
            break
        dataset = next(lines)
        mens = [''] * N
        p = ''
        indices = cycle(range(N))
        for card, i in zip(dataset, indices):
            match card:
                case 'M':
                    mens[i] += card
                case 'S':
                    p += card + mens[i]
                    mens[i] = ''
                case _:
                    mens[i] += card + p
                    p = ''
        print(*sorted(map(len, mens)), len(p))

if __name__ == '__main__':
    process_input()