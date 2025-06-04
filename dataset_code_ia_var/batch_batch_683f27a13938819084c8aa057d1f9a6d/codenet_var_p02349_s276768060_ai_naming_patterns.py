num_elements, num_queries = map(int, input().split())

ft_array = [0] * (num_elements + 1)

def ft_update(index, value):
    while index <= num_elements:
        ft_array[index] += value
        index += index & -index

def ft_query(index):
    result = 0
    while index:
        result += ft_array[index]
        index -= index & -index
    return result

query_results = []
for query_index in range(num_queries):
    query_input = input()
    if query_input[0] == "1":
        target_index = int(query_input[2:])
        query_results.append(str(ft_query(target_index)))
    else:
        start_index, end_index, update_value = map(int, query_input[2:].split())
        ft_update(start_index, update_value)
        if end_index < num_elements:
            ft_update(end_index + 1, -update_value)

for result in query_results:
    print(result)