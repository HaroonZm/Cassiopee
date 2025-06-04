input_list_length = int(input())
input_list_values = [int(x) for x in input().split()]
query_list_length = int(input())
query_list_values = [int(x) for x in input().split()]

match_count = 0

for query_value in query_list_values:
    if query_value in input_list_values:
        match_count += 1

print(match_count)