def resolve():
    a, b = input().split()
    c = int(a+b)
    num = pow(c, 0.5)
    if int(num) == num:
        print("Yes")
    else:
        print("No")
resolve()