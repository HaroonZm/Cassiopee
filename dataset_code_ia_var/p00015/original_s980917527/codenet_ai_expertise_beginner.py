n = int(input())
i = 0
while i < n:
    a = int(input())
    b = int(input())
    s = a + b
    s_str = str(s)
    if len(s_str) > 80:
        print("overflow")
    else:
        print(s_str)
    i = i + 1