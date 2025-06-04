num1, num2, num3 = map(int, input().split())
sum_nums = num1 + num2 + num3
max_num = max(num1, num2, num3)
if max_num * 2 == sum_nums:
    print("Yes")
else:
    print("No")