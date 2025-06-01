n = int(input())
i = 0
while i < n:
    a = input()
    b = input()
    c = int(a) + int(b)
    c_str = "{}".format(c)
    if len(c_str) > 80:
        print("overflow")
    else:
        print(c_str)
    i += 1