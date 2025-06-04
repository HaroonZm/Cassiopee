growth_rate, offset, initial_population = map(int, input().split())

current_population = initial_population

for iteration_number in range(10):

    current_population = growth_rate * current_population - offset

    print(current_population)