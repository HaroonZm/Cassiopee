input_n = int(input())
input_list = list(map(int, input().split()))
query_count = int(input())
for query_index in range(query_count):
    start_index, end_index, search_value = map(int, input().split())
    sublist = input_list[start_index:end_index]
    occurrence_count = sublist.count(search_value)
    print(occurrence_count)