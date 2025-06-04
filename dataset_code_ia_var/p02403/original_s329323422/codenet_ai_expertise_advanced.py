from sys import stdin
from itertools import islice, repeat

def main():
    lines = map(str.split, stdin)
    for h, w in map(lambda x: map(int, x), lines):
        if not (h or w):
            break
        row = '#' * w
        print('\n'.join(repeat(row, h)) + '\n')

if __name__ == '__main__':
    main()