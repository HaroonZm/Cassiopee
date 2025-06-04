input_count = int(input())
value_list = [int(item) for item in input().split()]

index_first = -1
index_second = -1

for index_outer in range(input_count):
    for index_inner in range(input_count):
        if index_outer != index_inner and abs(value_list[index_outer] - value_list[index_inner]) % (input_count - 1) == 0:
            index_first, index_second = index_outer, index_inner

print(value_list[index_first], value_list[index_second])