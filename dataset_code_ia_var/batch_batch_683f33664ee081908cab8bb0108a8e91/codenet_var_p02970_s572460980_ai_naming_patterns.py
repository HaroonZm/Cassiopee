n_value, d_value = map(int, input().split())
range_span = 2 * d_value + 1
required_steps = (n_value - 1) // range_span + 1
print(required_steps)