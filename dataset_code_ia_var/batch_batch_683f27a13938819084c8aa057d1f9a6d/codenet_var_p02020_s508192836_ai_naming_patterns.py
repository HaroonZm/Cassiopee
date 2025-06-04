input_count = int(input())
number_list = list(map(int, input().split()))
total_sum = sum(number_list)
if total_sum % 2 == 0:
    print(total_sum // 2)
else:
    number_list.sort()
    min_odd_value = None
    for current_value in number_list:
        if current_value % 2 == 1:
            min_odd_value = current_value
            break
    print((total_sum - min_odd_value) // 2)