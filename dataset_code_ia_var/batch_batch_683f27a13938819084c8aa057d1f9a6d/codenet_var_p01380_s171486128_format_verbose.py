number_of_problems = int(input())

problem_list = []
add_problem_to_list = problem_list.append

for problem_index in range(number_of_problems):
    
    time_required, deadline = map(int, input().split(" "))
    
    # Store as (deadline, time_required) tuple to sort by deadline
    add_problem_to_list((deadline, time_required))

problem_list.sort()

# dp[solved][score]: minimum total time to solve 'solved' problems
# Initialize all values as infinity except dp[0]
minimum_time_for_solved_problems = [float('inf')] * (number_of_problems + 1)
minimum_time_for_solved_problems[0] = 0

for problem_deadline, problem_time_required in problem_list:
    
    updated_minimum_time = list(minimum_time_for_solved_problems)
    
    for solved_count in range(1, number_of_problems + 1):
        
        if minimum_time_for_solved_problems[solved_count - 1] + problem_time_required <= problem_deadline:
            
            updated_minimum_time[solved_count] = min(
                minimum_time_for_solved_problems[solved_count],
                minimum_time_for_solved_problems[solved_count - 1] + problem_time_required
            )
    
    minimum_time_for_solved_problems = updated_minimum_time

maximum_solved_problems = 0

for solved_count in range(number_of_problems + 1):
    
    if minimum_time_for_solved_problems[solved_count] < float('inf'):
        maximum_solved_problems = solved_count

print(maximum_solved_problems)