from math import gcd

number_of_elements = int(input())

integer_list = list(map(int, input().split()))

greatest_common_divisor = integer_list[0]

for index in range(1, number_of_elements):
    greatest_common_divisor = gcd(greatest_common_divisor, integer_list[index])

print(greatest_common_divisor)