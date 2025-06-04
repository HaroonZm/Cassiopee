from math import ceil

input_total_value, group_a_size, group_a_cost, group_b_size, group_b_cost = map(int, input().split())

group_a_total_cost = ceil(input_total_value / group_a_size) * group_a_cost
group_b_total_cost = ceil(input_total_value / group_b_size) * group_b_cost

if group_a_total_cost > group_b_total_cost:
    print(group_b_total_cost)
else:
    print(group_a_total_cost)