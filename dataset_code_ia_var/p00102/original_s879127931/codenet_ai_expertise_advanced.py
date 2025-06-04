from sys import stdin
from itertools import tee

def main():
    while True:
        n_line = next(stdin)
        n = int(n_line)
        if n == 0:
            break
        rows = [list(map(int, stdin.readline().split())) for _ in range(n)]
        cols = list(map(list, zip(*rows)))
        row_sums = [r + [sum(r)] for r in rows]
        col_sums = [list(c) + [sum(c)] for c in cols]
        last_row = [sum(col) for col in zip(*rows)]
        total_sum = sum(last_row)
        last_row.append(total_sum)
        result = [r for r in row_sums]
        result.append(last_row)
        for i, line in enumerate(result):
            print(''.join(f'{x:5}' for x in line))
main()