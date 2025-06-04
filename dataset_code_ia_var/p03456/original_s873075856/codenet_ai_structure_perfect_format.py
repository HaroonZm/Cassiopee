a, b = input().split()
num = int(a + b) ** 0.5
if num.is_integer():
    print("Yes")
else:
    print("No")