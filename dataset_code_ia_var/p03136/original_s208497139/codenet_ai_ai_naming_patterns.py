input_n = int(input())

input_list = list(map(int, input().split()))

max_value = max(input_list)

max_index = input_list.index(max_value)
input_list.pop(max_index)

sum_others = sum(input_list)

if sum_others > max_value:
    print("Yes")
else:
    print("No")