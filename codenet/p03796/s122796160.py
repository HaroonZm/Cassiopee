import math

n = int(input())

power = math.factorial(n)
div = (10 ** 9) + 7

print(power % div)