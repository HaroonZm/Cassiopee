from sys import stdin

def chess_pattern(rows, cols):
    line_even = ''.join('#.'[(j % 2)] for j in range(cols))
    line_odd  = ''.join('.#'[(j % 2)] for j in range(cols))
    lines = [line_even if i % 2 == 0 else line_odd for i in range(rows)]
    return '\n'.join(lines)

for line in stdin:
    try:
        rows, cols = map(int, line.split())
        if rows == 0 and cols == 0:
            break
        print(chess_pattern(rows, cols), end='\n\n')
    except ValueError:
        continue