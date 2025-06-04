num_initial, step_distance = map(int, input().split())

counter_steps = 0
while num_initial > 0:
    num_initial -= (2 * step_distance + 1)
    counter_steps += 1

print(counter_steps)