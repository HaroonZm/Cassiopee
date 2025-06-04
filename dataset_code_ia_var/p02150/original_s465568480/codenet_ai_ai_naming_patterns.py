val_initial, val_decrement, val_target = [int(val_input) for val_input in input().split()]

step_difference = val_initial - val_decrement
step_count = max(0, (val_target - val_decrement)) // step_difference
result_value = val_target + step_count * val_decrement
print(result_value % 1000000007)