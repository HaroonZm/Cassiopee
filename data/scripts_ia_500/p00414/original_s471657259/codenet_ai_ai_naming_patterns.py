initial_length, iterations_count = map(int, input().split())
string_input = input()
consecutive_oo_count = 0

for index in range(initial_length - 1):
    if string_input[index:index + 2] == "oo":
        consecutive_oo_count += 1

while iterations_count:
    initial_length += consecutive_oo_count * 3
    consecutive_oo_count *= 2
    iterations_count -= 1

print(initial_length)