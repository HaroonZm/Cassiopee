first_integer, second_integer, third_integer = map(int, input().split())

sum_first_and_second = first_integer + second_integer
sum_second_and_third = second_integer + third_integer
sum_third_and_first = third_integer + first_integer

minimum_sum_of_pairs = min(
    sum_first_and_second,
    sum_second_and_third,
    sum_third_and_first
)

print(minimum_sum_of_pairs)