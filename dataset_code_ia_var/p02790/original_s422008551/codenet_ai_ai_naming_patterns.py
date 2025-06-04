input_str_1, input_str_2 = input().split()

str1_mult_int2 = input_str_1 * int(input_str_2)
str2_mult_int1 = input_str_2 * int(input_str_1)

if str1_mult_int2 < str2_mult_int1:
    print(str1_mult_int2)
else:
    print(str2_mult_int1)