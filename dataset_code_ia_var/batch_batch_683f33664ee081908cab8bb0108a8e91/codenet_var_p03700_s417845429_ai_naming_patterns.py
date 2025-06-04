total_elements, value_a, value_b = map(int, input().split())
heights_list = [int(input()) for _ in range(total_elements)]
upper_bound = 10**9
lower_bound = 0
while lower_bound + 1 < upper_bound:
    mid_value = (upper_bound + lower_bound) >> 1
    reduced_heights = [max(0, height - mid_value * value_b) for height in heights_list]
    required_operations = sum(-(-reduced_height // (value_a - value_b)) for reduced_height in reduced_heights)
    if mid_value >= required_operations:
        upper_bound = mid_value
    else:
        lower_bound = mid_value
print(upper_bound)