length_initial, iterations = map(int, input().split())
count_double_o = 0
snake_string = input()
for index in range(length_initial - 1):
    if snake_string[index:index + 2] == "oo":
        count_double_o += 1
length_current = length_initial
for _ in range(iterations):
    length_current += count_double_o * 3
    count_double_o *= 2
print(length_current)