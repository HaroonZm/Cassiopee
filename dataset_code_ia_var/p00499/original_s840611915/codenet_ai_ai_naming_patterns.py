length_total = int(input())
count_a = int(input())
count_b = int(input())
unit_a = int(input())
unit_b = int(input())

quotient_a = count_a // unit_a
quotient_b = count_b // unit_b
remainder_a = count_a % unit_a
remainder_b = count_b % unit_b

if quotient_a >= quotient_b:
    if remainder_a == 0:
        print(length_total - quotient_a)
    else:
        print(length_total - quotient_a - 1)
else:
    if remainder_b == 0:
        print(length_total - quotient_b)
    else:
        print(length_total - quotient_b - 1)