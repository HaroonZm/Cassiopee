x = input()
parts = x.split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

if a == 1:
    if b == 1:
        if c == 0:
            print("Open")
        else:
            print("Close")
    else:
        if c == 1 and b == 0 and a == 0:
            print("Open")
        else:
            print("Close")
else:
    if b == 0 and c == 1 and a == 0:
        print("Open")
    else:
        print("Close")