a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])
while not (a == 0 and b == 0):
    h = b // a
    c_list = input().split()
    for c_str in c_list:
        c = int(c_str)
        if c < h:
            b = b - (h - c)
    print(b)
    a_b = input().split()
    a = int(a_b[0])
    b = int(a_b[1])