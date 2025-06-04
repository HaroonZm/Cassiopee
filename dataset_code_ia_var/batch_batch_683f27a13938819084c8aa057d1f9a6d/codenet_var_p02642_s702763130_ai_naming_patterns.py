input_length = int(input())
input_numbers = list(map(int, input().split()))
input_numbers.sort()
max_value = max(input_numbers)

status_flags = [0] * (max_value + 1)

for number in input_numbers:
    if status_flags[number] != 0:
        status_flags[number] = 2
        continue
    if status_flags[number] == 0:
        status_flags[number] = 1
        for multiplier in range(1, max_value // number):
            status_flags[(multiplier + 1) * number] = 2

result_count = status_flags.count(1)
print(result_count)