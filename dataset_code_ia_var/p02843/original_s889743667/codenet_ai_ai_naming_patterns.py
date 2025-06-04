target_value = int(input())

reachable_flags = [0 for _ in range(target_value + 1)]
reachable_flags[0] = 1

for current_sum in range(target_value):
    if reachable_flags[current_sum] == 1:
        for add_value in range(100, 106):
            next_sum = current_sum + add_value
            if next_sum <= target_value:
                reachable_flags[next_sum] = 1

print(reachable_flags[target_value])