num1, num2, num3, num4 = map(int, input().split())
if (num1 == num2 and num3 == num4) or (num1 == num3 and num2 == num4) or (num1 == num4 and num2 == num3):
    print("yes")
else:
    print("no")