from fractions import gcd

value_n, value_x = map(int, input().split())
gcd_value = gcd(value_n, value_x)
difference_value = value_n - gcd_value
result_value = 3 * difference_value
print(result_value)