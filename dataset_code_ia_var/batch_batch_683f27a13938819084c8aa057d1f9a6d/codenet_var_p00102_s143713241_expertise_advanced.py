from itertools import islice, chain

def process():
    while True:
        try:
            n = int(raw_input())
        except:
            break
        if n == 0:
            break

        rows = [list(map(int, raw_input().split())) for _ in xrange(n)]
        row_sums = [sum(row) for row in rows]
        table = [row + [row_sum] for row, row_sum in zip(rows, row_sums)]

        col_sums = [sum(row[col] for row in rows) for col in xrange(n)]
        grand_total = sum(col_sums)
        summary_row = col_sums + [grand_total]
        table.append(summary_row)

        print '\n'.join(
            ''.join('{0:5d}'.format(x) for x in row)
            for row in table
        ) + '\n',

process()