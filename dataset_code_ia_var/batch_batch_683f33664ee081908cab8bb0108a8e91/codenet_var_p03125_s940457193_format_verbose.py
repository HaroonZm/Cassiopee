divisor, dividend = map(int, input().split())

if dividend % divisor == 0:
    print(divisor + dividend)
else:
    print(dividend - divisor)