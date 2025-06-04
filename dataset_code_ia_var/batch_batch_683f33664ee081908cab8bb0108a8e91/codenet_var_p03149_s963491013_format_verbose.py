user_input_numbers = list(map(int, input().split()))

required_numbers = [1, 9, 7, 4]

all_required_numbers_present = all(number in user_input_numbers for number in required_numbers)

if all_required_numbers_present:
    print("YES")
else:
    print("NO")