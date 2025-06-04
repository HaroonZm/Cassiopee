num_targets, atk_high, atk_low = map(int, input().split())
target_health_list = [int(input()) for _ in range(num_targets)]

def is_enough_rounds(rounds_needed):
    remaining_rounds = rounds_needed
    for initial_health in target_health_list:
        reduced_health = initial_health - atk_low * rounds_needed
        if reduced_health > 0:
            extra_hits = -(-reduced_health // (atk_high - atk_low))
            remaining_rounds -= extra_hits
        if remaining_rounds < 0:
            return False
    return True

min_rounds = 0
max_rounds = 10 ** 9
while max_rounds - min_rounds > 1:
    current_rounds = (min_rounds + max_rounds) // 2
    if is_enough_rounds(current_rounds):
        max_rounds = current_rounds
    else:
        min_rounds = current_rounds

print(max_rounds)