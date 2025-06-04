a, b = input().split()
a = int(a)
b = int(b)

if a + b == 15:
    print('+')
elif a * b == 15:
    print('*')
else:
    print('x')