number_of_inputs = int(input())

unique_sorted_lists = []

for _ in range(number_of_inputs):

    user_input_numbers = list(map(int, input().split()))

    user_input_numbers.sort()

    if unique_sorted_lists.count(user_input_numbers) == 0:

        unique_sorted_lists.append(user_input_numbers)

number_of_duplicates = number_of_inputs - len(unique_sorted_lists)

print(number_of_duplicates)