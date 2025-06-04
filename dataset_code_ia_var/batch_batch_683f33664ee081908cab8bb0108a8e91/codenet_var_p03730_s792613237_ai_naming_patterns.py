input_a, input_b, input_c = map(int, input().split())
max_iterations = input_b

is_solution_found = False
for current_iteration in range(max_iterations):
    if (current_iteration * input_a) % input_b == input_c:
        is_solution_found = True
        break

if is_solution_found:
    print("YES")
else:
    print("NO")