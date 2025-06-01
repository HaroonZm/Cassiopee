number_of_elements = int(input())
elements_list = list(map(int, input().split()))
maximum_consecutive_ones = 0
current_consecutive_ones_count = 0
for element in elements_list:
    if element == 1:
        current_consecutive_ones_count += 1
        if maximum_consecutive_ones <= current_consecutive_ones_count:
            maximum_consecutive_ones = current_consecutive_ones_count
    else:
        current_consecutive_ones_count = 0
print(maximum_consecutive_ones + 1)