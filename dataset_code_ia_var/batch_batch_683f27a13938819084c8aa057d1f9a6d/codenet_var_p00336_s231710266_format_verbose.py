MODULUS_VALUE = 1000000007

target_string = input()
subsequence_string = input()

length_of_target = len(target_string)
length_of_subsequence = len(subsequence_string)

number_of_subsequences = [
    [0] * (length_of_subsequence + 1)
    for _ in range(length_of_target + 1)
]

for target_prefix_length in range(length_of_target + 1):
    number_of_subsequences[target_prefix_length][0] = 1

for target_prefix_length in range(1, length_of_target + 1):
    for subsequence_prefix_length in range(1, length_of_subsequence + 1):
        number_of_subsequences[target_prefix_length][subsequence_prefix_length] = (
            number_of_subsequences[target_prefix_length - 1][subsequence_prefix_length] +
            number_of_subsequences[target_prefix_length - 1][subsequence_prefix_length - 1] *
            (target_string[target_prefix_length - 1] == subsequence_string[subsequence_prefix_length - 1])
        ) % MODULUS_VALUE

print(number_of_subsequences[length_of_target][length_of_subsequence])