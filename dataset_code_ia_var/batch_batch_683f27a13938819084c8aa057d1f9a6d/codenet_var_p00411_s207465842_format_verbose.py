user_input_values = input().split(" ")

initial_value = int(user_input_values[0])
time_duration = int(user_input_values[1])
rate_value = int(user_input_values[2])

result = (rate_value / initial_value) * time_duration

print(result)