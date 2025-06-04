import bisect

input_a, input_b, input_c, input_d, input_e, input_f = map(int, input().split())
set_water_volumes = set()
set_sugar_weights = set()

for factor_a in range(301):
    for factor_b in range(301):
        total_water = (factor_a * input_a + factor_b * input_b) * 100
        if 0 < total_water <= input_f:
            set_water_volumes.add(total_water)

for sugar_d in range(1500 // input_d + 1):
    for sugar_c in range((1500 - (sugar_d * input_d)) // input_c + 1):
        sugar_total = sugar_d * input_d + sugar_c * input_c
        if sugar_total <= input_f // 2 + 1:
            set_sugar_weights.add(sugar_total)

sorted_sugar_weights = sorted(list(set_sugar_weights))
best_result = [input_a * 100, 0]
max_concentration = 0

for water_volume in set_water_volumes:
    max_sugar_amount = sorted_sugar_weights[bisect.bisect(sorted_sugar_weights, min(input_f - water_volume, water_volume * input_e / 100)) - 1]
    mixture = [water_volume + max_sugar_amount, max_sugar_amount]
    if mixture[1] / mixture[0] > best_result[1] / best_result[0]:
        best_result = mixture

print('{} {}'.format(best_result[0], best_result[1]))