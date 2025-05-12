a, b = [int(i) for i in input().split()]

num = a * b

if num % 2 == 0:
    print("Even")
else:
    print("Odd")