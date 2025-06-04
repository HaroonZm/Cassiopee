node_count, query_count = map(int, input().split())
adjacency_list = [[] for _ in range(node_count)]
node_increment = [0] * node_count
for _ in range(node_count - 1):
    from_node, to_node = map(int, input().split())
    from_node -= 1
    to_node -= 1
    adjacency_list[from_node].append(to_node)

for _ in range(query_count):
    query_node, increment_value = map(int, input().split())
    query_node -= 1
    node_increment[query_node] += increment_value

result_values = [0] * node_count
stack = [(0, 0)]
while stack:
    current_node, accumulated_value = stack.pop()
    accumulated_value += node_increment[current_node]
    result_values[current_node] = accumulated_value
    for child_node in adjacency_list[current_node]:
        stack.append((child_node, accumulated_value))

for value in result_values:
    print(value, end=' ')
print()