input_count = int(input())
input_values = list(map(int, input().split()))

input_values.sort()

largest_value = input_values[-1]
sum_of_others = sum(input_values[:-1])

if largest_value < sum_of_others:
    print("Yes")
else:
    print("No")