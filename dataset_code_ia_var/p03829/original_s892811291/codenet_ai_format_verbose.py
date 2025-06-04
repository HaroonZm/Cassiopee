number_of_checkpoints, cost_per_kilometer, flat_cost = map(int, input().split())

checkpoint_positions = list(map(int, input().split()))

total_minimum_cost = sum([
    min(
        cost_per_kilometer * (checkpoint_positions[i + 1] - checkpoint_positions[i]),
        flat_cost
    )
    for i in range(number_of_checkpoints - 1)
])

print(total_minimum_cost)