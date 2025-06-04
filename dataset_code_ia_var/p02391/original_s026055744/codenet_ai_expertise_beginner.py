vals = input().split()
a = int(vals[0])
b = int(vals[1])

if a < b:
    print("a < b")
else:
    if a > b:
        print("a > b")
    else:
        print("a == b")