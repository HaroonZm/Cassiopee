from bisect import bisect_left

number_of_elements, number_of_queries = map(int, input().split())

array_elements = [int(element) for element in input().split()]

query_values = [int(input()) for _ in range(number_of_queries)]

start_index = (number_of_elements & 1) ^ 1
middle_index = number_of_elements // 2

current_window_sum = sum(array_elements[middle_index:])

partition_border_values = []
partition_sums = []

while start_index < middle_index:

    average_of_pair = (array_elements[start_index] + array_elements[middle_index]) // 2
    partition_border_values.append(average_of_pair)

    partition_sums.append(current_window_sum)

    current_window_sum = current_window_sum - array_elements[middle_index] + array_elements[start_index]

    start_index += 2
    middle_index += 1

partition_border_values.append(1e12)
partition_sums.append(current_window_sum)

for query in query_values:
    index_of_partition = bisect_left(partition_border_values, query)
    print(partition_sums[index_of_partition])