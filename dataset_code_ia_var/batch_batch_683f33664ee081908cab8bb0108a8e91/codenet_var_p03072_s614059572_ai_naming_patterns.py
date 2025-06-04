input_value = int(input())
input_list = list(map(int, input().split()))
current_max = 0
count_greater_equal = 0
for element in input_list:
    if current_max <= element:
        current_max = element
        count_greater_equal += 1
print(count_greater_equal)