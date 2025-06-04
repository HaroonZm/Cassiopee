read_ints = lambda: list(map(int, input().split()))
read_tuple = lambda: tuple(map(int, input().split()))

num_a, num_b, num_connections = read_tuple()
a_values = read_ints()
b_values = read_ints()

a_values_sorted = sorted(a_values)
b_values_sorted = sorted(b_values)

min_sum = a_values_sorted[0] + b_values_sorted[0]

for _ in range(num_connections):
    con_indices = read_ints()
    a_idx, b_idx, reduction = con_indices
    connection_sum = a_values[a_idx - 1] + b_values[b_idx - 1] - reduction
    min_sum = min(min_sum, connection_sum)

print(min_sum)