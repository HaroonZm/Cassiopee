user_input_value = int(input())
counter_value = 0
while (counter_value * (counter_value + 1) < 2 * user_input_value):
    counter_value += 1
print(counter_value)