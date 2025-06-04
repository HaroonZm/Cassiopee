numbers_list = sorted(list(map(int, input().split())), reverse=True)
largest_number = numbers_list[0]
sum_of_others = sum(numbers_list[1:])
if largest_number == sum_of_others:
    print("Yes")
else:
    print("No")