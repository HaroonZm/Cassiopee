num_elements, attack_power, reduction_power = (int(value) for value in input().split())
height_list = [0] * num_elements
for idx in range(num_elements):
    height_list[idx] = int(input())
max_height = max(height_list)
effective_attack = attack_power - reduction_power

def can_defeat_with_k(attacks_count):
    reduced_heights = [height - attacks_count * reduction_power for height in height_list]
    total_attacks_needed = 0
    for idx in range(num_elements):
        if reduced_heights[idx] > 0:
            total_attacks_needed += (reduced_heights[idx] - 1 + effective_attack) // effective_attack
    return total_attacks_needed <= attacks_count

binary_left = 0
binary_right = max_height // reduction_power + 1
while True:
    if binary_left == binary_right:
        break
    binary_mid = (binary_left + binary_right) // 2
    if can_defeat_with_k(binary_mid):
        binary_right = binary_mid
    else:
        binary_left = binary_mid + 1
print(binary_left)