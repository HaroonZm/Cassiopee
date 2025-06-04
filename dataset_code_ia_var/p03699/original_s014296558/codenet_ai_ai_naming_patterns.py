input_count = int(input())
number_list = [int(input()) for _ in range(input_count)]
number_list_sorted = sorted(number_list)
total_sum = sum(number_list)
if total_sum % 10 == 0:
    for index in range(len(number_list_sorted)):
        if number_list_sorted[index] % 10 == 0:
            continue
        else:
            number_list_sorted[index] = 0
            break
    else:
        print(0)
        exit(0)
print(sum(number_list_sorted))