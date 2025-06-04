MODULUS = 998244353
BASE = pow(10, 18, MODULUS)

def generate_grundy_counts():
    def compute_mex(node_index):
        mex_set = {}
        for neighbor in adjacency_list[node_index]:
            mex_set[grundy_values[neighbor]] = 1
        for grundy_candidate in range(total_nodes + 1):
            if grundy_candidate not in mex_set:
                return grundy_candidate

    edge_count = int(input())
    adjacency_list = [[] for _ in range(total_nodes)]
    for _ in range(edge_count):
        node_a, node_b = map(int, input().split())
        min_index = total_nodes - min(node_a, node_b)
        max_index = total_nodes - max(node_a, node_b)
        adjacency_list[min_index].append(max_index)
    grundy_values = [0] * total_nodes
    for node_index in range(total_nodes):
        grundy_values[node_index] = compute_mex(node_index)
    grundy_counts = [0] * 1024
    power_accumulator = 1
    for node_index in range(total_nodes - 1, -1, -1):
        power_accumulator = power_accumulator * BASE % MODULUS
        grundy_class = grundy_values[node_index]
        grundy_counts[grundy_class] = (grundy_counts[grundy_class] + power_accumulator) % MODULUS
    return grundy_counts

total_nodes = int(input())
grundy_counts_list_1 = generate_grundy_counts()
grundy_counts_list_2 = generate_grundy_counts()
grundy_counts_list_3 = generate_grundy_counts()

final_result = 0
for grundy_1 in range(1024):
    if grundy_counts_list_1[grundy_1] == 0:
        continue
    for grundy_2 in range(1024):
        if grundy_counts_list_2[grundy_2] == 0:
            continue
        xored_grundy = grundy_1 ^ grundy_2
        contribution = grundy_counts_list_1[grundy_1] * grundy_counts_list_2[grundy_2] % MODULUS
        contribution = contribution * grundy_counts_list_3[xored_grundy] % MODULUS
        final_result = (final_result + contribution) % MODULUS

print(final_result)