n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    c = a + b
    if len(str(c)) > 80:
        print("overflow")
    else:
        print(c)