num_elements = int(input())
element_list = list(map(int, input().split()))
num_queries = int(input())
for query_index in range(num_queries):
    range_start, range_end, target_value = map(int, input().split())
    sublist = element_list[range_start:range_end]
    occurrence_count = sublist.count(target_value)
    print(occurrence_count)