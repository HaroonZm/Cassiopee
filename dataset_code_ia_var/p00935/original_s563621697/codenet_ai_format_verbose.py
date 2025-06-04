number_of_digits, *individual_digits_list = map(int, open(0).read().split())

concatenated_digits_string = ''.join(map(str, individual_digits_list))

all_subnumbers_set = set()

for start_index in range(number_of_digits):
    for end_index in range(start_index + 1, number_of_digits + 1):
        subnumber_as_integer = int(concatenated_digits_string[start_index:end_index])
        all_subnumbers_set.add(subnumber_as_integer)

smallest_nonpresent_integer = 0

while smallest_nonpresent_integer in all_subnumbers_set:
    smallest_nonpresent_integer += 1

print(smallest_nonpresent_integer)