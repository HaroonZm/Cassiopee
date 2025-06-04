row_count, col_count = map(int, input().split())

line_list = []
for row_index in range(row_count):
    line_list.append(input())

border_line = "#" * (col_count + 2)
print(border_line)
for row_index in range(row_count):
    print("#" + line_list[row_index] + "#")
print(border_line)