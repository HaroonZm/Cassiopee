num_targets, atk_full, atk_reduced = map(int, input().split())
hp_list = [int(input()) for _ in range(num_targets)]

def is_attack_sufficient(num_main_attacks):
    total_secondary_attacks = 0
    for hp in hp_list:
        residual_hp = hp - atk_reduced * num_main_attacks
        if residual_hp <= 0:
            continue
        num_secondary = -(-residual_hp // (atk_full - atk_reduced))
        total_secondary_attacks += num_secondary
    if total_secondary_attacks > num_main_attacks:
        return False
    else:
        return True

left_bound, right_bound = -1, 10**9
while right_bound - left_bound > 1:
    mid_point = (left_bound + right_bound) // 2
    if is_attack_sufficient(mid_point):
        right_bound = mid_point
    else:
        left_bound = mid_point

print(right_bound)