input_n = int(input())
input_values_list = list(map(int, input().split()))
input_query_count = int(input())

for query_index in range(input_query_count):
    query_begin, query_end, query_value = map(int, input().split())

    sublist = input_values_list[query_begin:query_end]
    value_count = sublist.count(query_value)
    print(value_count)