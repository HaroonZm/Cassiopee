inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])

if a + b == 15:
    print("+")
else:
    if a * b == 15:
        print("*")
    else:
        print("x")