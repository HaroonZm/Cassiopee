from math import ceil

def check_feasibility(m_count):
    updated_health = health_list[:]
    for idx in range(num_targets):
        updated_health[idx] -= m_count * damage_b
    if not any(updated_health):
        return True
    remaining_attacks = 0
    for health_val in updated_health:
        if health_val > 0:
            remaining_attacks += ceil(health_val / (damage_a - damage_b))
    return remaining_attacks <= m_count

num_targets, damage_a, damage_b = map(int, input().split())
health_list = [int(input()) for _ in range(num_targets)]

left_bound = 0
right_bound = 10 ** 10

while abs(left_bound - right_bound) > 1:
    mid_val = (right_bound + left_bound) // 2
    if check_feasibility(mid_val):
        right_bound = mid_val
    else:
        left_bound = mid_val

print(right_bound)