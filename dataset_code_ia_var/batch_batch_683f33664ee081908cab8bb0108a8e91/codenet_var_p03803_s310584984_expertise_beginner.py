a, b = input().split()
a = int(a)
b = int(b)

if a == b:
    print("Draw")
else:
    if a == 1:
        print("Alice")
    elif b == 1:
        print("Bob")
    else:
        if a > b:
            print("Alice")
        else:
            print("Bob")