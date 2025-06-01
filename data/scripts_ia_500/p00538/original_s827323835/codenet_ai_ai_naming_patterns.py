import sys

sys.setrecursionlimit(10000)

input_length = int(input())
input_values = [int(input()) for index_loop in range(input_length)] * 3
dp_table = [[-1 for col_index in range(input_length * 2)] for row_index in range(input_length * 2)]

def depth_first_search(index_start, index_end):
    if dp_table[index_start][index_end] != -1:
        return dp_table[index_start][index_end]
    length_interval = index_end - index_start
    if length_interval == input_length - 1:
        dp_table[index_start][index_end] = 0
    elif length_interval % 2 == 0:
        if input_values[index_start - 1] > input_values[index_end + 1]:
            dp_table[index_start][index_end] = depth_first_search(index_start - 1, index_end)
        else:
            dp_table[index_start][index_end] = depth_first_search(index_start, index_end + 1)
    else:
        dp_table[index_start][index_end] = max(
            depth_first_search(index_start - 1, index_end) + input_values[index_start - 1],
            depth_first_search(index_start, index_end + 1) + input_values[index_end + 1]
        )
    return dp_table[index_start][index_end]

maximum_score = 0
for index_base in range(input_length):
    maximum_score = max(maximum_score, depth_first_search(index_base, index_base) + input_values[index_base])

print(maximum_score)