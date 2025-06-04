input_size_a, input_size_b = map(int, input().split())
input_list_a = list(map(int, input().split())) + [10**9 + 1]
input_list_b = list(map(int, input().split())) + [10**9 + 1]
result_list_intersection = []
result_list_union = []
index_a = 0
index_b = 0
for _ in range(input_size_a + input_size_b):
    value_a = input_list_a[index_a]
    value_b = input_list_b[index_b]
    if value_a < value_b:
        result_list_union.append(value_a)
        index_a += 1
    elif value_a == value_b:
        result_list_intersection.append(value_a)
        index_a += 1
    else:
        result_list_union.append(value_b)
        index_b += 1
print(len(result_list_intersection), len(result_list_union))
for value in result_list_intersection:
    print(value)
for value in result_list_union:
    print(value)