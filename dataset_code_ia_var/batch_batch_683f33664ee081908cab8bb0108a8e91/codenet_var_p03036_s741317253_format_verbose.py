initial_amount, deduction_amount, initial_value = map(int, input().split())

for iteration_number in range(1, 11):
    initial_value = initial_amount * initial_value - deduction_amount
    print(initial_value)