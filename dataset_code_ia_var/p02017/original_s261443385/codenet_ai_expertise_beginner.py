inputs = input().split()
h = int(inputs[0])
w = int(inputs[1])
x = int(inputs[2])
y = int(inputs[3])

if (h * w) % 2 == 1:
    if (x + y) % 2 == 1:
        print("No")
    else:
        print("Yes")
else:
    print("Yes")