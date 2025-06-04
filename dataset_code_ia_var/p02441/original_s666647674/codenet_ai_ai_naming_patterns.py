input_count = int(input())
input_sequence = list(map(int, input().split()))
query_count = int(input())
for query_index in range(query_count):
    range_start, range_end, target_value = map(int, input().split())
    print(input_sequence[range_start:range_end].count(target_value))