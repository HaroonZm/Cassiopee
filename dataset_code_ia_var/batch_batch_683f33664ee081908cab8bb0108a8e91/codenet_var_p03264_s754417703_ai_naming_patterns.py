input_value = int(input())
quotient, remainder = divmod(input_value, 2)
result = quotient * (quotient + remainder)
print(result)