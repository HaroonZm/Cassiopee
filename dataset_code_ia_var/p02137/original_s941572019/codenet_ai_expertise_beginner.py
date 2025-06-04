n = int(input())
if n % 500 == 0:
    print(n)
else:
    quotient = n // 500
    result = quotient * 500
    print(result)