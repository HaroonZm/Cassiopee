num_problems, time_limit = (int(value) for value in input().split())

min_cost = 1001
for problem_index in range(num_problems):
    current_cost, current_time = (int(value) for value in input().split())
    if current_time <= time_limit and current_cost < min_cost:
        min_cost = current_cost

if min_cost > 1000:
    print('TLE')
else:
    print(min_cost)