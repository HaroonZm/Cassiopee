row_count, column_count = map(int, input().split())
input_lines = [input() for _ in range(row_count)]
max_line_length = max(len(line) for line in input_lines)
border_line = '#' * max_line_length + '##'
print(border_line)
for current_line in input_lines:
    print('#' + current_line + '#')
print(border_line)