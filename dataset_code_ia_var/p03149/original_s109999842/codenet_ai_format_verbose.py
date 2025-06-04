input_numbers_as_strings = input().split()

input_numbers_as_integers = list(map(int, input_numbers_as_strings))

input_numbers_as_integers.sort()

constructed_number = (
    1000 * input_numbers_as_integers[0]
    + 100 * input_numbers_as_integers[3]
    + 10 * input_numbers_as_integers[2]
    + input_numbers_as_integers[1]
)

EXPECTED_VALUE = 1974

if constructed_number == EXPECTED_VALUE:
    print("YES")
else:
    print("NO")