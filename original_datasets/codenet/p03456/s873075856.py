a, b = input().split()
num = int(a + b)**0.5
print("Yes" if num.is_integer() else "No")