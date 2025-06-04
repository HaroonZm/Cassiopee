value_target, value_increment, value_decrement = [int(value_input) for value_input in input().split()]

if value_increment >= value_target:
    result_steps = 1
elif value_decrement >= value_increment:
    result_steps = -1
else:
    result_steps = 1 + ((value_target - value_decrement - 1) // (value_increment - value_decrement)) * 2
print(result_steps)