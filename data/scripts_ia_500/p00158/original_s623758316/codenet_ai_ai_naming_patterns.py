def collatz_step(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1

while True:
    user_input = int(input())
    if user_input == 0:
        break
    
    iteration_count = 0
    current_value = user_input
    while current_value != 1:
        current_value = collatz_step(current_value)
        iteration_count += 1
    print(iteration_count)