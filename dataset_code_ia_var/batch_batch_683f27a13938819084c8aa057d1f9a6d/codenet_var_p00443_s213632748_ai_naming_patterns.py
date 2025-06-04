def compute_gcd(value_a, value_b):
	while value_b != 0:
		remainder = value_a % value_b
		value_a, value_b = value_b, remainder
	return value_a

def compute_lcm(value_a, value_b):
	return value_a // compute_gcd(value_a, value_b) * value_b

def compute_weight(node_index):
	right_weight = compute_weight(nodes_list[node_index][2]) if nodes_list[node_index][2] > 0 else 1
	left_weight = compute_weight(nodes_list[node_index][3]) if nodes_list[node_index][3] > 0 else 1
	total_weight = compute_lcm(nodes_list[node_index][0] * right_weight, nodes_list[node_index][1] * left_weight)
	return total_weight // nodes_list[node_index][0] + total_weight // nodes_list[node_index][1]

while True:
	node_count = int(input())
	if node_count == 0:
		break
	parent_indices = [0] * (node_count + 1)
	nodes_list = [(0, 0, 0, 0)]
	for current_index in range(1, node_count + 1):
		value_p, value_q, index_r, index_b = map(int, input().split())
		nodes_list.append((value_p, value_q, index_r, index_b))
		if index_r > 0:
			parent_indices[index_r] = current_index
		if index_b > 0:
			parent_indices[index_b] = current_index
	for search_index in range(1, node_count + 1):
		if parent_indices[search_index] == 0:
			break
	print(compute_weight(search_index))