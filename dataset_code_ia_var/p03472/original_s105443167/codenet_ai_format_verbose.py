number_of_weapons, target_health = map(int, input().split())

attack_and_burst_list = [
    list(map(int, input().split()))
    for _ in range(number_of_weapons)
]

maximum_attack_power = max([
    attack_power
    for attack_power, burst_power in attack_and_burst_list
])

burst_powers_higher_than_attack = sorted([
    burst_power
    for _, burst_power in attack_and_burst_list
    if burst_power > maximum_attack_power
], reverse=True)

total_burst_damage = sum(burst_powers_higher_than_attack)

if total_burst_damage >= target_health:
    while total_burst_damage >= target_health:
        total_burst_damage -= burst_powers_higher_than_attack.pop()
    minimum_attacks_required = len(burst_powers_higher_than_attack) + 1
else:
    remaining_health_after_bursts = target_health - total_burst_damage
    additional_attacks_required = (remaining_health_after_bursts - 1) // maximum_attack_power + 1
    minimum_attacks_required = additional_attacks_required + len(burst_powers_higher_than_attack)

print(minimum_attacks_required)