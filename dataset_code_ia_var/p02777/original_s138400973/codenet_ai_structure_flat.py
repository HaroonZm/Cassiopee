s = input().split()
num = [int(i) for i in input().split()]
u = input()
num1 = num[0]
num2 = num[1]
if s[0] == u:
    nums = num1 - 1
    print(str(nums) + " " + str(num2))
else:
    if s[1] == u:
        nums = num2 - 1
        print(str(num1) + " " + str(nums))