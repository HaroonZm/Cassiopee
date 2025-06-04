from sys import stdin

def process():
    for line in stdin:
        n = int(line)
        if n == 0:
            break
        total = [0] * (n + 1)
        rows = [list(map(int, stdin.readline().split())) for _ in range(n)]
        output = []
        for row in rows:
            row_sum = sum(row)
            row.append(row_sum)
            total = [x + y for x, y in zip(total, row)]
            output.append(''.join(f"{val:5d}" for val in row))
        output.append(''.join(f"{val:5d}" for val in total))
        print('\n'.join(output))
        
process()