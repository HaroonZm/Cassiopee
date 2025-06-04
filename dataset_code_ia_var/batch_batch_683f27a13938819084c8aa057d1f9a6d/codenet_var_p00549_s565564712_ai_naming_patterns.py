input_length = int(input())
input_string = input()
count_jo = 0
count_oi = 0
count_j = 0
count_o = 0
count_i = 0
count_joi = 0
list_j_cumsum = []
list_o_cumsum = []
list_i_cumsum = []
for char in input_string:
    if char == "J":
        count_j += 1
    elif char == "O":
        count_o += 1
        count_jo += count_j
    else:
        count_i += 1
        count_oi += count_o
        count_joi += count_jo
    list_j_cumsum.append(count_j)
    list_o_cumsum.append(count_o)
    list_i_cumsum.append(count_i)

max_ji = max(list_j_cumsum[idx] * (list_i_cumsum[-1] - list_i_cumsum[idx]) for idx in range(input_length))
print(count_joi + max(count_jo, count_oi, max_ji))