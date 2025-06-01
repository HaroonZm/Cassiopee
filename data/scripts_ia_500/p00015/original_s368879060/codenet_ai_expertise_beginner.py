n = int(input())
for k in range(n):
    a = input()
    b = input()
    c = int(a) + int(b)
    c_str = str(c)
    if len(c_str) > 80:
        print("overflow")
    else:
        print(c)