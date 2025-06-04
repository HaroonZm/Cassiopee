import sys
from itertools import cycle, islice

def pattern(h, w):
    base = ['#', '.']
    row_patterns = [islice(cycle(base if i % 2 == 0 else base[::-1]), w) for i in range(h)]
    return '\n'.join(''.join(row) for row in row_patterns)

def main():
    for line in sys.stdin:
        h, w = map(int, line.split())
        if not (h or w):
            break
        print(pattern(h, w), end='\n\n')

main()